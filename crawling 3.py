import requests
from bs4 import BeautifulSoup

print("="*22,"요일별로 어떤 웹툰이 있는지 더 알고 싶다면?","="*22)

사전 = {}
for j in ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]:
    res = requests.get(f"https://comic.naver.com/webtoon/weekdayList?week={j}")
    soup = BeautifulSoup(res.text, "html.parser")

    for i in soup.select(".thumb > a"):
        제목 = i.get("title")
        ID = i.get("href").split("=")[1].split("&")[0]
        사전[제목] = ID
print(사전)

for i in 사전:
    res = requests.get(f"https://comic.naver.com/webtoon/list?titleId={사전[i]}")
    soup = BeautifulSoup(res.text, "html.parser")

    작가 = soup.select_one(".wrt_nm").text.strip()
    소개 = soup.select_one(".detail > p").text
    장르 = soup.select_one(".genre").text
    연령 = soup.select_one(".age").text

    print("="*30)
    print(f"제목\t{i}")
    print(f"작가\t{작가}")
    print(f"장르\t{장르}")
    print(f"연령\t{연령}")
    print("="*30)
    print(소개)
    print()