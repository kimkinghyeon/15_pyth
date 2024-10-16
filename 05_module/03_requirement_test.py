# selenium => 웹페이지를 자동으로 탐색할 수 있게 도와주는 라이브러리
# webdriver-manager => 브라우저에 맞는 드라이버를 관리할 수 있게 해주는 라이브러리

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# chrome 웹드라이버 설정
service = Service(ChromeDriverManager().install())
dirver = webdriver.Chrome(service=service)

# Google 홈페이지 열기
dirver.get("https://www.google.com")

# 검색하기
search_box = dirver.find_element(By.NAME,'q')

# 검색어 입력
search_box.send_keys('오점머')

# 검색 실행
search_box.send_keys(Keys.RETURN)
time.sleep(10)

# 브라우저 종료
dirver.quit()



