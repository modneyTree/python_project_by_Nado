from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Chrome 브라우저 옵션 설정
options = webdriver.ChromeOptions()
options.headless = False  # 브라우저 창을 띄우도록 설정
options.add_argument("window-size=1920x1080")  # 창 크기 설정

# Chrome 드라이버 시작
browser = webdriver.Chrome(options=options)
browser.maximize_window()  # 브라우저 창 최대화

# 1. 네이버 이동
browser.get("https://www.naver.com")
time.sleep(1)  # 페이지가 로드될 시간을 잠깐 기다림

# 2. 검색창에 검색어 입력
search_box = browser.find_element(By.NAME, "query")  # 검색창 요소 선택
search_box.send_keys("파이썬")  # 검색어 입력

# 3. Enter 키 입력으로 검색 실행
search_box.send_keys(Keys.RETURN)  # Enter 키 입력

# 4. 검색 결과 페이지에서 HTML 출력
time.sleep(2)  # 페이지가 로드될 시간을 기다림
print(browser.page_source)  # 페이지 소스 출력 (확인용)

# 5. 브라우저 종료
browser.quit()
