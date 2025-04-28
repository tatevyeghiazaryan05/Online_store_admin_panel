import os

import main
from fastapi import APIRouter, Depends, HTTPException, status, Form, File, UploadFile
from schemas import DrinkSchema, DrinkNameChangeSchema, DrinkImageChangeSchema, DrinkKindChangeSchema, DrinkPriceChangeSchema, DrinkCategoryChangeSchema, GetFeedbacksSchema
from security import pwd_context, get_current_admin
from fastapi.responses import FileResponse
from datetime import datetime, timedelta, date
import shutil


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
    upload_dir = "drink_images"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    if file:
        l = file.filename.split(".")

        image_name = l[0] + " " + str(datetime.now()).replace(":", "") + "." + l[-1]
        file_path = f"{upload_dir}/{image_name}"

        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

        except PermissionError:
            raise HTTPException(status_code=500, detail="File write error")

    else:
        image_name = "drinks.jpg"

    main.cursor.execute(
        """INSERT INTO drinks (name, kind, price, image, category) VALUES (%s, %s, %s, %s, %s)""",
        (name, kind, price, image_name, category)
    )
    main.conn.commit()

    return {"message": "Drink added successfully", "image_url": image_name}


@admin_router.delete("/api/drinks/delete/by-id/{drink_id}")
def delete_drink(drink_id: int, token=Depends(get_current_admin)):
    main.cursor.execute("SELECT * FROM drinks WHERE id = %s",
                        (drink_id,))
    drink = main.cursor.fetchone()
    drink = dict(drink)
    image_name = drink.get("image")
    print(f"image_name is :{image_name}")
    main.cursor.execute("DELETE FROM drinks WHERE id = %s",
                        (drink_id,))
    main.conn.commit()

    if image_name == "drinks.jpg":
        return

    file_path = f"drink_images/{image_name}"
    print(f"file_path:{file_path}")

    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("File does not exist.")


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


@admin_router.put("/api/drinks/change/drink_image/by/drink_id/{drink_id}")
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


@admin_router.get("/api/drinks/get/image/by/id/{drink_id}")
def get_images(drink_id: int):
    main.cursor.execute("SELECT image FROM drinks WHERE id=%s",
                        (drink_id,))
    result = main.cursor.fetchone()
    if result is None:
        return "Drink not found "

    image_name = result['image']
    image_path = os.path.join("drink_images", image_name)

    if not os.path.exists(image_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Image file not found"
        )

    return FileResponse(path=image_path, media_type="image/jpeg", filename=image_name)


@admin_router.get("/admins/api/get/feedback/{start_date}/{end_date}", status_code=200)
def get_feedback(start_date: date, end_date: date):
    main.cursor.execute("SELECT * FROM feedback WHERE created_at >= %s AND created_at <= %s",
                        (start_date, end_date))
    feedbacks = main.cursor.fetchall()
    return feedbacks


@admin_router.get("/api/admin/get/orders/by/id/{order_id}")
def get_orders(order_id: int):
    main.cursor.execute("SELECT * FROM orders WHERE id=%s",
                        (order_id,))


@admin_router.get("/api/admin/get/orders/by/date/{start_date}/{end_date}")
def get_order_by_date(start_date: datetime.date, end_date: datetime.date):

    main.cursor.execute("SELECT * FROM orders WHERE created_at >= %s AND created_at <= %s",
                        (start_date, end_date))
    orders = main.cursor.fetchall()

    return orders


@admin_router.get("/api/admin/get/orders/by/price/{min_price}/{max_price}")
def get_order_by_date(min_price: float,  max_price: float):
    main.cursor.execute("SELECT * FROM orders WHERE total_price >= %s AND total_price <= %s",
                        (min_price, max_price))
    orders = main.cursor.fetchall()

    return orders
