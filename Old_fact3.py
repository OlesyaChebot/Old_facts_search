from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('https://proprognozy.ru/football/')

# Вывести сколько матчей к проверке
matches = driver.find_elements_by_css_selector('.match-panel-link ')
range=len(matches)
print(range,"футбольных матчей к проверке")

# Найти список ссылок всех матчей
from selenium.common.exceptions import TimeoutException
elems = driver.find_elements_by_css_selector('.match-panel-link ')
links = [elem.get_attribute('href') for elem in elems]
# print(links)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

for m,i in enumerate(links):
    driver.implicitly_wait(15)
    driver.get(i)
    try:forecast=WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".nav.nav-pills.nav-justified.overflow-auto.flex-nowrap.mt-md-4>li:nth-child(2)")))
    except TimeoutException:
        print(m+1,"из",range,"СТРАНИЦА НЕ ЗАГРУЖАЕТСЯ!",i)
    else:
        forecast.click()
    driver.execute_script("window.scrollBy(0, 1500);")
    try:new_view=WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".forecast-item-rate-total.text-gray")))
    except TimeoutException:
        print(m+1,"из",range,"НЕТ ФАКТОВ В НОВОМ ПРЕДСТАВЛЕНИИ!",i)
    else:
        print(m+1,"из",range,"Факты представлены в новом виде",i)
driver.quit()
import winsound
duration = 2000
frequency = 2000
winsound.Beep(frequency, duration)

