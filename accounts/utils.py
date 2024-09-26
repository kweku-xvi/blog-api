import os
from dotenv import load_dotenv
from trycourier import Courier

load_dotenv()

client = Courier(auth_token=os.getenv('AUTH_TOKEN'))

def send_verification_email(first_name:str, email:str, link:str):
    client.send_message(
        message={
            "to": {
            "email": email,
            },
            "template": os.getenv('EMAIL_VERIFICATION_TEMPLATE'),
            "data": {
            "firstName": first_name,
            "link": link,
            },
        }
    )


def send_password_reset_mail(first_name:str, email:str, link:str):
    client.send_message(
        message={
            "to": {
            "email": email,
            },
            "template": os.getenv('PASSWORD_RESET_TEMPLATE'),
            "data": {
            "firstName": first_name,
            "link": link,
            },
        }
    )