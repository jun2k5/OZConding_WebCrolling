from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

import time


#동적 크롤링
#무한 스크롤 구현 페이지에서
#초기 화면에 보이는 결과 게시물은 30개정도.
#스크롤을 아래로 내리면 나오는 결과 게시물은 60개로 추가된다.
#정적 크롤링은 빠르다.
#동적 크롤링은 사용자가 직접 웹사이트에 들어가 얻는 정보와
#동일한 정보를 크롤링 할 수 있다.

#최대한 정적 크롤링으로 구현하는 것이 좋다.

#동적 크롤링을 위해서 셀레니움 오픈소스 사용

keyword = input("검색어를 입력해주세요 : ")
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="+keyword

options_ = Options() #객체 생성, 인스턴스화
options_.add_experimental_option("detach", True) #자동종료하지 않음 옵션 추가

driver = webdriver.Chrome(options=options_) # webdriver로 테스트용 Chrome브라우저 생성

driver.get(url) #브라우저에 url을 입력하고 가져올 수 있는 정보를 get요청
time.sleep(2)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(0.5)
    #웹 상에서 기능을 수행하게하기 위해서 JS코드를 사용해야한다.

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
result = soup.select(".sds-comps-vertical-layout.sds-comps-full-layout.pSGytgqBoO_qDdSTbXs9")

for i in result:
    ad = i.select_one(".fender-ui_228e3bd1.fender-ui_c8f4a785")
    if not ad:
        writer = i.select_one(".sds-comps-text.sds-comps-text-ellipsis.sds-comps-text-ellipsis-1").text
        title = i.select_one(".sds-comps-text.sds-comps-text-ellipsis.sds-comps-text-ellipsis-1.sds-comps-text-type-headline1.sds-comps-text-weight-sm").text
        dsc = i.select_one(".sds-comps-text.sds-comps-text-type-body1.sds-comps-text-weight-sm").text
        link = i.select_one(".fender-ui_228e3bd1.zsOIyFgaikMtT9gmM_tR")["href"]

        print(f"제목 : {title}")
        print(f"작성자 : {writer}") 
        print(f"요약 : {dsc}")
        print(f"링크 : {link}")
        # print(f"작성자 : {writer.text}") #html태그를 제외한 텍스트 출력
        print("============")


time.sleep(1)
driver.quit()


print(len(result))

#우리가 보는 html파일코드를 viewport라고 한다.
#무한 스크롤은 스크롤을 맨 밑으로 내릴수록
# BODY태그의 높이가 늘어난다.

#JS코드가 유일하게 웹에서 동작을 만들 수 있음

















