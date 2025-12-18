# 프론트엔드단으로 대부분 JSON형태로 보낸다.
# dict나 list로 데이터로 넘겨준다.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#select나 select_one과 비슷한 역할
from selenium.webdriver.common.by import By 
#키보드 키입력 api
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

import pymysql

import time

import dotenv
import os


dotenv.load_dotenv()
HOST_NAME = os.getenv("HOST_NAME")
USER_NAME = os.getenv("USER_NAME")
DB_PWD = os.getenv("DB_PWD")

url = "https://kream.co.kr/"

options_ = Options()
options_.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options_)
driver.get(url)
time.sleep(1)

# 요소 가져오기 (select_one)
# driver.find_element(By.CSS_SELECTOR, "클래스 이름")
# 요소 클릭하기 click()
# driver.find_element(By.CSS_SELECTOR, "클래스 이름").click() 
driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
time.sleep(1)

#요소에 데이터 입력하기 send_keys("검색어")
#driver.find_element(By.CSS_SELECTOR, "클래스 이름").send_keys("슈프림")
#요소에 키 입력하기 send_keys(Keys.키보드키)
#driver.find_element(By.CSS_SELECTOR, "클래스 이름").send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림" + Keys.ENTER)
time.sleep(1)

#페이지 다운키로 스크롤 아래로 내리기 Keys.PAGE_DOWN
for i in range(20):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

#스크롤로 확장된 페이지 html 가져오기
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
items = soup.select(".product_card")

product_list = [] # 리스트 초기화 => 초기화 : 준비를 시킨다.



for item in items:
    category = "상의"
    #item.select_one("클래스명:not(제외할클래스명)")
    product_name = item.select_one(".text-lookup.display_paragraph.line_break_by_truncating_tail.text-element:not(.semibold)").text
    product_brand = item.select_one(".semibold.text-lookup.display_paragraph.line_break_by_truncating_tail.text-element").text
    #item.select_one("div.클래스명 p") 클래스명을 가진 div 안의 p 태그 요소 선택
    product_price = item.select_one("div.price-info-container p").text

    product = [category, product_brand, product_name, product_price]
    product_list.append(product)


driver.quit()

# driver.execute_script("")

conn = pymysql.connect(
    host = HOST_NAME,
    user = USER_NAME,
    password = DB_PWD,
    db = 'kream',
    charset= 'utf8mb4',
)

def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ())
        connection.commit()


for i in product_list:
    query = "INSERT INTO kream (category, brand, product_name, price) VALUES (%s, %s, %s, %s)"
    execute_query(conn, query, (i[0],i[1],i[2],i[3]))
























