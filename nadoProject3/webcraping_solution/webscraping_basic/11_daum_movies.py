import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"    
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class": "thumb_img"})

    for idx, image in enumerate(images):
        image_url = image["src"]
        
        # data:로 시작하는 URL은 건너뜁니다.
        if image_url.startswith("data:"):
            print("  <data URL은 제외합니다>")
            continue
        
        # //로 시작하는 URL은 https:로 수정합니다.
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        
        print(image_url)  # 이미지 URL 확인용 출력
        
        # 이미지 다운로드
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        
        with open(f"movie_{year}_{idx + 1}.jpg", "wb") as f:
            f.write(image_res.content)
        
        if idx >= 4:  # 상위 5개 이미지까지만 다운로드
            break
