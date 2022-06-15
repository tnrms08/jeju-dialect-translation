import requests, bs4
from pandas import Series, DataFrame
import requests, bs4
import pandas as pd
from konlpy.tag import Hannanum


# API 주소.. 단어 총 7159개라서 pageSize=7159
xmlUrl = 'http://www.jeju.go.kr/rest/JejuDialectService/getJejuDialectServiceList?authApiKey=&startPage=1&pageSize=7159'

# requests 이용해서 API 받기. 인코딩은 utf-8이용~
response = requests.get(xmlUrl).text.encode('utf-8')

# 뷰티풀수프(태그 데이터 출력.. 아마두) 쓰기. API가 xml 형식이라서 뒤에 xml
xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')




# item 태그에 한 단어에 대한 설명 있음. item 태그들 다 찾기
rows = xmlobj.findAll('item')

# item 태그 안에 있는 거 각각 접근
columns = rows[0].find_all()

# 값 저장할 빈 리스트들 만들기
rowList = [] #
nameList = [] #이름
columnList = [] #

# 아이템 총 개수
rowsLen = len(rows)




# rowLen만큼
for i in range(0, rowsLen):

    # 태그 안 내용 각각 접근
    columns = rows[i].find_all()

    # 각 태그 안 요소 개수    
    columnsLen = len(columns)


    # columnsLoen만큼
    for j in range(0, columnsLen):
        # 첫 번째 행 데이터 값 수집 시에만 컬럼 값 저장(모든 컬럼헤더(rows[0], rows[1], ...)는 동일한 값을 가짐. 매번 반복할 필요 없음)
        if i == 0:
            nameList.append(columns[j].name)
        # 컬럼값은 모든 행 값 저장    
        eachColumn = columns[j].text
        # columnList에 추가
        columnList.append(eachColumn)
    #저장한 값 rowList에
    rowList.append(columnList)
    # 다음 row의 값을 넣기 위해 비움
    columnList = []    
    


# 파싱한 값들 모아서 데이터프레임으로
result = pd.DataFrame(rowList, columns=nameList)

#필요한 컬럼만 가져오기(사전 만드려면 index(초성별 구분)도 추가하기~~)
result = result.loc[:, ['name', 'siteName', 'index', 'contents', 'engContents']]

result.to_csv('C:\\Users\\user\\jeju-dialect-translation\\csv_flie\\dict2.csv', sep=',', na_rep='NaN')
              
result2 = result[['siteName', 'contents']]
result2 = result2.sort_values(['siteName'])
result2.to_csv('C:\\Users\\user\\jeju-dialect-translation\\csv_flie\\dict3.csv', sep=',', na_rep='NaN')

