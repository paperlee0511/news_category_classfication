from sys import executable

from numpy.f2py.rules import arg_rules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

from job01_crawling_headline import title_tags

options = ChromeOptions()

options.add_argument('lang=ko_KR')

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = 'https://news.naver.com/section/100'
driver.get(url)
# time.sleep(5)
button_xpath ='//*[@id="newsct"]/div[4]/div/div[2]'
# //*[@id="newsct"]/div[4]/div/div[2]
# //*[@id="newsct"]/div[5]/div/div[2]
for i in range(15):
    time.sleep(0.5)
    driver.find_element(By.XPATH, button_xpath).click()

time.sleep(5)

for i in range(1, 6):
    for j in range(1, 7):
        title_path = '//*[@id="newsct"]/div[4]/div/div[1]/div[{}]/ul/li[{}]/div/div/div[2]/a/strong'.format(i,j)
        #예외 처리
        try :
            title = driver.find_element(By.XPATH, title_path).text
            print(title)
        except:
            print('error', i , j)

# Xpath 의 규칙 찾기
# '//*[@id="_SECTION_HEADLINE_LIST_zydng"]/li[1]/div/div/div[2]/a/strong # 헤드라인 뉴스'
# '//*[@id="newsct"]/div[4]/div/div[1]/div[4]/ul/li[1]/div/div/div[2]/a/strong'
# '//*[@id="newsct"]/div[4]/div/div[1]/div[4]/ul/li[2]/div/div/div[2]/a/strong'
# '//*[@id="newsct"]/div[4]/div/div[1]/div[5]/ul/li[2]/div/div/div[2]/a/strong'
# '//*[@id="newsct"]/div[4]/div/div[1]/div[5]/ul/li[3]/div/div/div[2]/a/strong'
