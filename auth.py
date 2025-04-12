import main
from fastapi import APIRouter, HTTPException, status, Form, UploadFile, File
from security import pwd_context, create_access_token
import shutil
from schemas import AdminLoginSchema, AdminPasswordRecover
from pydantic import EmailStr
from email_service import send_verification_email
import os

auth_routher = APIRouter()

Upload_Dir = "images"


@auth_routher.post("/api/admin/auth/sign-up")
def admin_signup(
        name: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        file: UploadFile = File(None),
):
    Upload_Dir = "images"
    if not os.path.exists(Upload_Dir):
        os.makedirs(Upload_Dir)

    main.cursor.execute("SELECT * FROM admins WHERE email = %s", (email,))
    if main.cursor.fetchone():
        raise HTTPException(status_code=400, detail="Email already registered.")

    image_name = "default.jpg"

    if file:
        file_path = f"{Upload_Dir}/{file.filename}"

        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            image_name = file.filename
        except PermissionError:
            raise HTTPException(status_code=500, detail="File write error")

        hashed_password = pwd_context.hash(password)

        main.cursor.execute("INSERT INTO admins (name, email, password, image_name) VALUES (%s,%s,%s,%s)",
                            (name, email, hashed_password, image_name))
        main.conn.commit()
        return "Sign Up Successfully!!"


@auth_routher.post("/api/admin/auth/login")
def admin_login(login_data: AdminLoginSchema):
    email = login_data.email
    password = login_data.password

    main.cursor.execute("SELECT * FROM admins WHERE email = %s",
                        (email,))
    admin = main.cursor.fetchone()
    admin = dict(admin)
    admin_password_db = admin.get("password")

    if not pwd_context.verify(password,admin_password_db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="password is not correct!!"
        )
    else:
        admin_id_db = admin.get("id")
        admin_email_db = admin.get("email")
        return create_access_token({"id": admin_id_db,
                                    "email": admin_email_db})


@auth_routher.get("/api/admin/password/change/code/{email}")
def send_password_change_code_to_email(email: EmailStr):
    try:
        main.cursor.execute("SELECT * FROM admins WHERE email=%s",
                            (email,))
        user = main.cursor.fetchone()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="server error"
        )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="not such user!"

        )

    verification_code = send_verification_email(email)
    main.cursor.execute("INSERT INTO changepasswordcodes (code,email) VALUES(%s,%s)",
                        (verification_code, email))

    main.conn.commit()


@auth_routher.post("/api/admin/password/recovery/by/email")
def password_recovery(recover_data: AdminPasswordRecover):
    code = recover_data.code
    new_password = pwd_context.hash(recover_data.new_password)

    try:
        main.cursor.execute("SELECT * FROM changepasswordcodes WHERE code=%s",
                        (code,))
        data = main.cursor.fetchone()
        data = dict(data)

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="server error"
        )

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="code is incorrect!"

        )

    main.cursor.execute("UPDATE admins SET password =%s WHERE email=%s",
                        (new_password, data["email"]))

    main.conn.commit()

    main.cursor.execute("DELETE FROM changepasswordcodes WHERE code = %s",
                        (code,))
    main.conn.commit()
    return "Recovered successfully!!"


#TODO code must has 15 minuts exparation time date  and if code date ends it must delete afto
