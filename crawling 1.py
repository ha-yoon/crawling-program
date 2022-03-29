from bs4 import BeautifulSoup
st = """<html>
    <body class="a">
        <div id="hello1" here1="안녕하세요~">하윤이의 깃허브에 오신걸 환영합니다🙌</div>
        <div class="hello2" here2="크롤링이란 무엇인가요?">웹페이지에서 내가 필요한 데이터들을 쏙쏙 추출해오는 작업입니다~</div>
        <div id="b">
            <span id="c">그럼 제가 원하는 정보를 뽑으러 같이 가볼까요?😜</span>
        </div>
        <span>슝~😆 정보는 crawling 2.py 에서 확인해주세요~!</span>
    </body>
</html>"""
soup = BeautifulSoup(st, "html.parser")
print(soup.select_one("#hello1").get("here1"))
print(soup.select_one("#hello1").text)
print(soup.select_one(".hello2").get("here2"))
print(soup.select_one(".hello2").text)
print(soup.select_one("span").text)
print(soup.select_one("body > span").text)
