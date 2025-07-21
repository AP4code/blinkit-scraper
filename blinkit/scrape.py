import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = uc.ChromeOptions()
options.headless = False
driver = uc.Chrome(options=options)

try:
    driver.get("https://blinkit.com/cn/munchies/nachos/cid/1237/316")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "img")))

    html = driver.execute_script("return document.documentElement.outerHTML")

    with open("C:/Users/adiun/Documents/blinkit/page.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Full HTML saved.")

finally:
    driver.quit()
