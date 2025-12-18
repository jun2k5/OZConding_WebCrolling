import requests
from bs4 import BeautifulSoup



def main():
    keyword = input("검색어를 입력해주세요 : ")
    url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="+ keyword
    req = requests.get(url) #기능에 가깝다.
    #    print(req.text)
    html = req.text #req.text 화면을 구성하는 html 코드
    soup = BeautifulSoup(html, "html.parser") # parser 트리구조로 만들어서 파있너에게 학습 할 수 있도록 도와줌
    result = soup.select(".sds-comps-vertical-layout.sds-comps-full-layout.pSGytgqBoO_qDdSTbXs9")
    #클래스명이나 아이디명을 통해 우리가 원하는 값을 모두 가져오고 list와 비슷한 형태의 데이터타입으로 반환해준다.
    #클래스명일 경우 앞에 .을 붙이고 아이디일 경우 #을 붙인 후 공백을 없애준다.
    

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


if __name__ == "__main__":
    main()


