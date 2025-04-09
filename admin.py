import os

import main
from fastapi import APIRouter, Depends, HTTPException, status, Form, File, UploadFile
from schemas import DrinkSchema, DrinkNameChangeSchema
from security import pwd_context, get_current_admin

admin_router = APIRouter()


@admin_router.post("/api/drink/add")
def drink_add(name: str = Form(...),
              kind: str = Form(...),
              price: float = Form(...),
              file: UploadFile = File(None),
              token=Depends(get_current_admin)
              ):
    image_name = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shutterstock.com%2Fsearch%2Fsoft-drink-logo&psig=AOvVaw3L6aeMiZdyNZ4snBqX7n0x&ust=1743663632411000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMjI2bLjuIwDFQAAAAAdAAAAABAV"

    if file:
        upload_dir = "static/images"
        os.makedirs(upload_dir, exist_ok=True)























    main.cursor.execute("""INSERT INTO drinks (name,kind,price,image) VALUES(%s,%s,%s,%s)""",
                      (name, kind, price, image_name)) #TODO image has to be link but user has to give it like image
    main.conn.commit()
    return {"message": "Drink added successfully"}


@admin_router.delete("/api/drinks/delete/by-id/{drink_id}")
def delete_drink(drink_id: int, token=Depends(get_current_admin)):
    main.cursor.execute("DELETE FROM drinks WHERE id = %s",
                        (drink_id,))
    main.conn.commit()
    return "Deleted successfully!! "


@admin_router.put("/api/drinks/change/by/drink_id/{drink_id}")
def change_drinks(drink_id: int, change_data: DrinkNameChangeSchema, token=Depends(get_current_admin)):
    main.cursor.execute("UPDATE drinks SET name = %s WHERE id = %s", (change_data.name, drink_id))
    main.conn.commit()
    return "Drink updated successfully!!"
