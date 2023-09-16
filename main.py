import requests
from webscrapperselenium import get_info_from_alibaba
from farsi_tools import standardize_persian_text

url1 = "https://www.alibabatravels.co/international/THRALL-ISTALL?adult=1&child=0&infant=0&departing=1402-06-24&gclid=CjwKCAjw3oqoBhAjEiwA_UaLtoYiIeKS0j2qZ-LSs6OlWchjtdkPjGWNrKEyMC7hPG_gvYIJFSHotBoCxVYQAvD_BwE"
url2 = "https://www.alibabatravels.co/international/ISTALL-THRALL?adult=1&child=0&infant=0&departing=1402-06-24&gclid=CjwKCAjw3oqoBhAjEiwA_UaLtiRQYlfn4AhWUc70sYAfZ_YF8zv8lL_hSe2FxPSzLoABSu4yY-FsIBoCMm8QAvD_BwE"


def send_sms(sender: str, receptor: str, text: str):
    data = {'from': sender, 'to': receptor, 'text': text}
    response = requests.post('https://console.melipayamak.com/api/send/simple/1a4cef018cd24c45ae3dd7ad9e1c5ea3', json=data)
    print(response.json())


flight_info = ""
f = get_info_from_alibaba(url2)
leg1 = f["مبدا"] # NOQA
leg2 = f["مقصد"] # NOQA

for key, value in f.items():
    flight_info += f"{key} : {value} | "

sample_text = standardize_persian_text(f"پرواز {leg1}  به {leg2} با مشخصات زیر پیدا شد:\n" # NOQA
                                       f"{flight_info}\n"
                                       f"از سفرت جا نمونی \N{slightly smiling face}") # NOQA


