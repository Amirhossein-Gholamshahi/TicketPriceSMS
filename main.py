import requests
from webscrapperselenium import get_info_from_alibaba
from farsi_tools import standardize_persian_text
import time


def send_sms(sender: str, receptor: str, text: str):
    data = {'from': sender, 'to': receptor, 'text': text}
    response = requests.post('https://console.melipayamak.com/api/send/simple/1a4cef018cd24c45ae3dd7ad9e1c5ea3', json=data)
    print(response.json())


flight_info = ""
for key, value in get_info_from_alibaba().items():
    flight_info += f"{key} : {value} | "
sample_text = standardize_persian_text(f"پرواز استانبول به تهران با مشخصات زیر پیدا شد:\n" # NOQA
                                       f"{flight_info}\n"
                                       f"از سفرت جا نمونی \N{slightly smiling face}") # NOQA


