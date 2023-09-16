from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

url1 = "https://www.alibabatravels.co/international/THRALL-ISTALL?adult=1&child=0&infant=0&departing=1402-06-24&gclid=CjwKCAjw3oqoBhAjEiwA_UaLtoYiIeKS0j2qZ-LSs6OlWchjtdkPjGWNrKEyMC7hPG_gvYIJFSHotBoCxVYQAvD_BwE"
url2 = "https://www.alibabatravels.co/international/ISTALL-THRALL?adult=1&child=0&infant=0&departing=1402-06-24&gclid=CjwKCAjw3oqoBhAjEiwA_UaLtiRQYlfn4AhWUc70sYAfZ_YF8zv8lL_hSe2FxPSzLoABSu4yY-FsIBoCMm8QAvD_BwE"


def get_info_from_alibaba(url):
    try:
        custom_options = webdriver.ChromeOptions()
        custom_options.add_argument("headless")
        path = "C:\Program Files (x86)\chromedriver.exe" # NOQA
        driver_service = Service(executable_path=path)
        driver = webdriver.Chrome(service=driver_service, options=custom_options)
        driver.get(url)
        price = driver.find_element(By.CSS_SELECTOR, "#app > div.wrapper > main > div > div.layout-sidebar__main > section > div:nth-child(4) > div:nth-child(1) > div > div.available-card__action.flex.justify-center.items-center > div > span > strong").text
        flight_info = driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div[1]/section/div[3]/div[1]/div/div[1]/div/div/div/div/div[2]/div").text.split('\'')
        driver.quit()
        l = "".join(flight_info).split("\n")
        if url == url1:
            return {"قیمت": f"  {price} ریال ", "ایرلاین": l[0], "ساعت خروج": l[1], "زمان پرواز": l[2], "مبدا": "تهران", "مقصد": "استانبول" } # NOQA
        elif url == url2:
            return {"قیمت": f"  {price} ریال ", "ایرلاین": l[0], "ساعت خروج": l[1], "زمان پرواز": l[2], "مبدا": "استانبول","مقصد": "تهران"}  # NOQA
    except Exception as exp:
        print(exp)


