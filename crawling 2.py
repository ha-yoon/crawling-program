import requests
from bs4 import BeautifulSoup

print("제가 추출하고자 했던 정보는 바로 요즘 푹~ 빠진 웹툰 인데요👍\n여러분들께도 추천해드리고자 간략한 소개 준비했습니다👏")
print("="*35,"첫번째 추천작", "="*35)

res = requests.get ("https://comic.naver.com/webtoon/list?titleId=557672&weekday=thu")
soup = BeautifulSoup(res.text, "html.parser")

print(soup.select_one(".title").text.strip())
print(soup.select_one(".wrt_nm").text.strip())
print(soup.select_one("p").text.strip())
print(soup.select_one(".genre").text.strip())
print(soup.select_one(".age").text.strip())


print("="*35,"두번째 추천작", "="*35)
res = requests.get ("https://comic.naver.com/webtoon/list?titleId=694946")
soup = BeautifulSoup(res.text, "html.parser")

print(soup.select_one(".title").text.strip())
print(soup.select_one(".wrt_nm").text.strip())
print(soup.select_one("p").text.strip())
print(soup.select_one(".genre").text.strip())
print(soup.select_one(".age").text.strip())
print("="*85)

