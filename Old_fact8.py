from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('https://функционирующий сайт, поэтому не могу дать ссылку, чтобы не перегружать сервер')

# Вывести сколько матчей к проверке
matches = driver.find_elements_by_css_selector('.match-panel-link ')
range=len(matches)
print(range,"футбольных матчей, открытых дефолтом в листинге")

# Закрыть рекламы, чтобы не перекрывали элементы листинга
close_gift = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.js-gift-close-btn')))

close_btns=driver.find_elements_by_css_selector('.reset-btn.icon-close')
WebDriverWait(driver, 50).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '.reset-btn.icon-close')))
for close_btn in close_btns:
    close_btn.click()

# Вывести в консоль количество кнопок листинга
hidden_matches=driver.find_elements_by_css_selector('.clickable_item.table-head__all ')
range1=len(hidden_matches)
print(range1,"кнопок открытия/закрытия листинга")
# print(hidden_matches[0])

# Закрыть всплывающую рекламу, если открылась
from selenium.common.exceptions import NoSuchElementException
driver.implicitly_wait(15)
try: modal_btn=driver.find_element_by_css_selector('.btn-reset.icon-close')
except NoSuchElementException:pass
else: modal_btn.click()

# Нажать поочередно на все листинги, чтобы в DOOM загрузились все матчи, а не только открытые дефолтом
import time
for hidden_match in hidden_matches:
    # if hidden_match==hidden_matches[9]:
    #     break
    # else:
    time.sleep(1)
    WebDriverWait(driver, 25).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.clickable_item.table-head__all ')))
    hidden_match.click()


# Найти массив ссылок всех матчей
hidden_elems = driver.find_elements_by_css_selector('.match-panel-link ')
hidden_links = [hidden_elem.get_attribute('href') for hidden_elem in hidden_elems]
# print(links)
#
# Зайти поочередно по каждой ссылке, нажать кнопку Прогноз, найти серую надпись
for m,i in enumerate(hidden_links,start=15):
    if i==hidden_links[49]:
        break
    else:
        driver.implicitly_wait(15)
        driver.get(i)
        try:hidden_forecast=WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".nav.nav-pills.nav-justified.overflow-auto.flex-nowrap.mt-md-4>li:nth-child(2)")))
        except TimeoutException:
            print(m+1,"из",range1,"СТРАНИЦА НЕ ЗАГРУЖАЕТСЯ!",i)
        else:
            hidden_forecast.click()
        driver.execute_script("window.scrollBy(0, 1500);")
        try:new_view=WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".forecast-item-rate-total.text-gray")))
        except TimeoutException:
            print(m+1,"из",range1,"НЕТ ФАКТОВ В НОВОМ ПРЕДСТАВЛЕНИИ!",i)
        else:
            print(m+1,"из",range1,"Факты представлены в новом виде",i)

driver.quit()
# Сообщить звуковым сигналом о завершении проверки
import winsound
duration = 2000
frequency = 2000
winsound.Beep(frequency, duration)





