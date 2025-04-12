import smtplib
import random
from email.message import EmailMessage


# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "tatevikyeghiazaryann5@gmail.com"
EMAIL_PASSWORD = "klcm ecsh nfcb xhzs"

verification_codes = {}


def generate_verification_code():
    """Generate a random 6-digit verification code"""
    return str(random.randint(100000, 999999))


def send_verification_email(user_email):
    """Send verification code to user email"""
    code = generate_verification_code()

    msg = EmailMessage()
    msg["Subject"] = "Click here "
    msg["From"] = EMAIL_SENDER
    msg["To"] = user_email
    msg.set_content(f"{code}")

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        return code
    except Exception as e:
        print("Error sending email:", e)
        return False


