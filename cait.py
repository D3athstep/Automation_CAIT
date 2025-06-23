from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

repeat_count = 10
url = "https://developer.api.tekxal.com/"
xpath_element = "/html/body/div/div/div/nav/div/div/div[1]/div/ul/li[3]/a"
wait_between_clicks = 2

# 1️⃣ Create a Service instance
service = Service(ChromeDriverManager().install())

# 2️⃣ Pass it to the WebDriver
driver = webdriver.Chrome(service=service)

try:
    # ✅ Main Loop
    for i in range(repeat_count):
        try:
            driver.get(url)
            time.sleep(wait_between_clicks)
            element = driver.find_element(By.XPATH, xpath_element)
            element.click()
            print(f"✅ Clicked element {i + 1}/{repeat_count}")

            time.sleep(wait_between_clicks)

        except Exception as e:
            print(f"❌ Error on iteration {i + 1}: {e}")

finally:
    # Always close the browser
    time.sleep(3)
    driver.quit()
