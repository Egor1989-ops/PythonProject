from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Создание экземпляра веб-драйвера (например, Chrome)
driver = webdriver.Chrome()
# Создание объекта WebDriverWait с веб-драйвером и временем ожидания 10 секунд
wait = WebDriverWait(driver, 10)
