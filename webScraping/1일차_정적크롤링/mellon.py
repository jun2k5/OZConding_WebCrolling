#최신 100곡 추출하기
import requests
from bs4 import BeautifulSoup
import dotenv
import os

url = "https://www.melon.com/new/index.htm"

dotenv.load_dotenv()
user_agent = os.getenv("USER_AGENT")

hdr = {'User-agent' : user_agent}

req = requests.get(url, headers=hdr)
#print(req)  #406상태코드 반환, 사용자 정보가 없다면 멜론에서는 크롤링을 허용해주지않음
            #따라서 user_agent정보를 추가하여 사람이 접속함을 알림 
            
html = req.text
soup = BeautifulSoup(html, "html.parser")
result = soup.select(".wrap_song_info")
#print(result)
count = 1

#파일 초기화
with open("new_songs_list.txt", "w", encoding="UTF-8-sig") as f:
    f.write("최신곡 50\n")

for i in result:
    try:
        song_name = i.select_one(".ellipsis.rank01").text
        artist = i.select_one(".checkEllipsis").text
    except AttributeError:
        continue

    #멜론은 최신곡 목록을 item - non_item 형식으로 
    #하나의 정보를 내보내면 다음 정보는 None으로 처리한다.
    #때문에 None 값이 들어오면 AttributeError을 발생시킨다.
    #이는 예외처리로 해결하였다.

#파일 작성
    with open("new_songs_list.txt", "a", encoding="UTF-8-sig") as f:
        f.write(str(count) + '. \n')
        f.write(f"곡 이름 : {song_name}".replace('\n',''))
        f.write("\n")
        f.write(f"가수 : {artist}".replace('\n',''))
        f.write("\n")
        f.write("===============\n")

    count += 1
    #곡이름과 가수명의 값이 앞에 \n이 붙은상태로 들어온다.
    #replace로 엔터값을 삭제하였다.




