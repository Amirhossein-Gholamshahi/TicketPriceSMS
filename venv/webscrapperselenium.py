from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
def get_info_from_alibaba():
    try:
        url1 = "https://www.alibabatravels.co/international/THRALL-ISTALL?adult=1&child=0&infant=0&departing=1402-06-24&gclid=CjwKCAjw3oqoBhAjEiwA_UaLtoYiIeKS0j2qZ-LSs6OlWchjtdkPjGWNrKEyMC7hPG_gvYIJFSHotBoCxVYQAvD_BwE"
        url2 = "https://www.alibabatravels.co/international/ISTALL-THRALL?adult=1&child=0&infant=0&departing=1402-06-24&gclid=CjwKCAjw3oqoBhAjEiwA_UaLtiRQYlfn4AhWUc70sYAfZ_YF8zv8lL_hSe2FxPSzLoABSu4yY-FsIBoCMm8QAvD_BwE"
        custom_options = webdriver.ChromeOptions()
        custom_options.add_argument("headless")
        path = "C:\Program Files (x86)\chromedriver.exe"
        driver_service = Service(executable_path=path)
        driver = webdriver.Chrome(service=driver_service, options=custom_options)
        driver.get(url2)
        price = driver.find_element(By.CLASS_NAME, "text-secondary-400").text
        flight_info = driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div[1]/section/div[3]/div[1]/div/div[1]/div/div/div/div/div[2]/div").text.split('\'')
        driver.quit()
        l = "".join(flight_info).split("\n")
        return {"قیمت": f"  {price} ریال ", "ایرلاین": l[0], "ساعت خروج": l[1], "زمان پرواز": l[2]}
    except Exception as exp:
        print(exp)


