from bs4 import BeautifulSoup   # HTML 파싱용
import requests                 # 웹 요청용 
import re                       # 정규화 표현식
import pandas as pd             # 데이터프레임 처리용
import datetime                 # 파일명에 날짜 사용

# 카테고리 정의 및 빈 데이터 프레임 준비
# catogory : 각 뉴스 섹션을 영어로 저장한 리스트
# df_titles : 센션별 뉴스 제목을 하나로 합치기 위한 빈 데이터프레임
category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']
df_titles = pd.DataFrame()
# url = 'https://news.naver.com/section/100' # 정치 섹션의 주소

# 6개 뉴스 섹션 순회
for i in range(6):
    # 100 ~ 105까지 총 6개의 뉴스 섹션을 순회
    url = 'https://news.naver.com/section/10{}'.format(i) # 경제 섹션의 주소
    # 서버한테 주소를 요청
    resp = requests.get(url) # HTML요청 및 파싱, 페이징 요청
    soup = BeautifulSoup(resp.text, features= 'html.parser') # 파싱
    # print(list(soup))
    title_tags = soup.select('.sa_text_strong') # 앞의 . 은 class를 의미
    # print(list(title_tags)) # strong 태그만 긁어옴 # 이제 문자열만 뽑아오면 됨

    # 뉴스 제목 텍스트만 추출
    titles = []
    for tag in title_tags:
        titles.append(tag.text)
    print(titles) # 정치 셋션이니 Plitics를 붙이면 될것

    # 섹션별 데이터프레임 생성 및 결핮
    # titles : 하나의 섹션에 대한 뉴스 제목 리스트
    # df_section_titles : 하나의 섹션에 대한 뉴스 DataFrame
    # category[i] : 해당 섹션의 카테고리 추가
    # df_titles : 모든 섹션 뉴스 제목을 뉴적해서 합친결과
    df_section_titles = pd.DataFrame(titles, columns=['titles'])
    df_section_titles['category'] = category[i]
    df_titles = pd.concat([df_titles, df_section_titles],
                          axis = 'rows', ignore_index= True)

# 결과 출력 및 저장
print(df_titles.head())
df_titles.info()    # 데이터프레임 구조 확인
print(df_titles['category'].value_counts()) # 각 센셕별 뉴스 갯수 확인
# csv 파일 저장
df_titles.to_csv('./crawling_data/naver_headline_news{}.csv'.format(
                 datetime.datetime.now().strftime('%Y%m%d')), index = False)


