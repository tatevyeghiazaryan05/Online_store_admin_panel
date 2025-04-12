import os

import main
from fastapi import APIRouter, Depends, HTTPException, status, Form, File, UploadFile
from schemas import DrinkSchema, DrinkNameChangeSchema, DrinkImageChangeSchema, DrinkKindChangeSchema, DrinkPriceChangeSchema, DrinkCategoryChangeSchema
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
              category: str = Form(...),
              file: UploadFile = File(None),
              token=Depends(get_current_admin)
              ):
    image_name = "http://127.0.0.1:8000/api/images/get_image/drinks.jpg"

    if file:
        upload_dir = "drink_images"
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, file.filename)

        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        image_url = f"http://127.0.0.1:8000/api/images/get_image/{file.filename}"

    main.cursor.execute(
        """INSERT INTO drinks (name, kind, price, image, category) VALUES (%s, %s, %s, %s, %s)""",
        (name, kind, price, image_name, category)
    )
    main.conn.commit()

    return {"message": "Drink added successfully", "image_url": image_name}


@admin_router.delete("/api/drinks/delete/by-id/{drink_id}")
def delete_drink(drink_id: int, token=Depends(get_current_admin)):
    main.cursor.execute("SELECT image FROM drinks WHERE id = %s", (drink_id,))
    deleted_image = main.cursor.fetchone()
   #todo
    main.conn.commit()
    return "Deleted successfully!! "


@admin_router.put("/api/drinks/change/drink_name/by/drink_id/{drink_id}")
def change_drinks(drink_id: int, change_data: DrinkNameChangeSchema, token=Depends(get_current_admin)):
    main.cursor.execute("UPDATE drinks SET name = %s WHERE id = %s", (change_data.name, drink_id))
    main.conn.commit()
    return "Drink name updated successfully!!"


@admin_router.put("/api/drinks/change/drink_kind/by/drink_id/{drink_id}")
def change_drinks(drink_id: int, change_data: DrinkKindChangeSchema, token=Depends(get_current_admin)):
    main.cursor.execute("UPDATE drinks SET kind = %s WHERE id = %s", (change_data.kind, drink_id))
    main.conn.commit()
    return "Drink kind updated successfully!!"


@admin_router.put("/api/drinks/change/drink_price/by/drink_id/{drink_id}")
def change_drinks(drink_id: int, change_data: DrinkPriceChangeSchema, token=Depends(get_current_admin)):
    main.cursor.execute("UPDATE drinks SET price = %s WHERE id = %s", (change_data.price, drink_id))
    main.conn.commit()
    return "Drink price updated successfully!!"


@admin_router.put("/api/drinks/change/drink_category/by/drink_id/{drink_id}")
def change_drinks(drink_id: int, change_data: DrinkCategoryChangeSchema, token=Depends(get_current_admin)):
    main.cursor.execute("UPDATE drinks SET category = %s WHERE id = %s", (change_data.category, drink_id))
    main.conn.commit()
    return "Drink category updated successfully!!"


@admin_router.put("/api/drinks/change/drink_kind/by/drink_id/{drink_id}")
def change_drinks(drink_id: int, file: UploadFile = File(...), token=Depends(get_current_admin)):

    if file:
        upload_dir = "drink_images"
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        image_url = f"http://127.0.0.1:8000/api/images/get_image/{file.filename}"

        main.cursor.execute("UPDATE drinks SET image = %s WHERE id = %s", (image_url, drink_id))
        main.conn.commit()
        return "Drink image updated successfully!!"


