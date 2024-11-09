import requests
from bs4 import BeautifulSoup

# URL 설정
url = "https://finance.naver.com/marketindex/"

# 페이지 요청
response = requests.get(url)
response.raise_for_status()  # 요청 에러 발생 시 예외 처리

# BeautifulSoup을 사용해 HTML 파싱
soup = BeautifulSoup(response.text, "lxml")

# 주요 환율 정보 가져오기
exchange_data = soup.select(".market1 .data")

print("네이버 금융 - 주요 환율 정보")
for data in exchange_data:
    currency = data.select_one("h3.h_lst").get_text()  # 통화 종류
    value = data.select_one(".value").get_text()       # 환율 값
    print(f"{currency}: {value}")
