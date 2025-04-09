import os

import main
from fastapi import APIRouter, Depends, HTTPException, status, Form, File, UploadFile
from schemas import DrinkSchema, DrinkNameChangeSchema
from security import pwd_context, get_current_admin
from fastapi.responses import FileResponse

admin_router = APIRouter()


@admin_router.get("/api/images/get_image/{image_name}")
def get_image_name(image_name: str):
    return FileResponse(f"./drink_images/{image_name}")


@admin_router.post("/api/drink/add")
def drink_add(name: str = Form(...),
              kind: str = Form(...),
              price: float = Form(...),
              file: UploadFile = File(None),
              token=Depends(get_current_admin)
              ):
    image_name = "http://127.0.0.1:8000/api/images/get_image/drinks.jpg"

    if file:
        upload_dir = "static/images"
        os.makedirs(upload_dir, exist_ok=True)
        filename = file.filename  #TODO give a category,image link have to put in database and image has to add in our drink_images folder

    main.cursor.execute("""INSERT INTO drinks (name,kind,price,image) VALUES(%s,%s,%s,%s)""",
                      (name, kind, price, filename))
    main.conn.commit()
    return {"message": "Drink added successfully"}


@admin_router.delete("/api/drinks/delete/by-id/{drink_id}")
def delete_drink(drink_id: int, token=Depends(get_current_admin)):
    main.cursor.execute("DELETE FROM drinks WHERE id = %s",
                        (drink_id,))
    main.conn.commit()
    return "Deleted successfully!! "#TODO image also has to be deleted


@admin_router.put("/api/drinks/change/by/drink_id/{drink_id}")
def change_drinks(drink_id: int, change_data: DrinkNameChangeSchema, token=Depends(get_current_admin)):
    main.cursor.execute("UPDATE drinks SET name = %s WHERE id = %s", (change_data.name, drink_id))
    main.conn.commit()
    return "Drink updated successfully!!"#TODO Update all columns
