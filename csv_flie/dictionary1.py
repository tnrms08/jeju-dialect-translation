from pandas import Series, DataFrame
import requests, bs4
import pandas as pd
from konlpy.tag import Hannanum


#csv 파일 읽기
path ="C:\\Users\\user\\jeju-dialect-translation\\csv_flie\\dict2.csv"
dict = pd.read_csv(path, sep=",", encoding = 'UTF-8')

index=["IS01S", "IS01D", "IS02S", "IS03S", "IS03D" ,"IS04S", "IS05S", "IS06S", "IS06D" , "IS07S", "IS07D", "IS08S", "IS09S", "IS09D", "IS10S", "IS11S", "IS12S", "IS13S", "IS14S"]


# 빈 데이터 프레임 만들기
results = pd.DataFrame(columns = {'name', 'contents'})

# print(results)


# index 리스트 길이만큼 반복
for i in range(len(index)):
    #임시 변수
    x = dict[dict['index'] == index[i]]

    # x 데이터프레임에서 siteName과 contents만 남겨두기
    x = x[['siteName', 'contents']]

    # results 데이터프레임과 x 합치기(위아래로)
    results = pd.concat([results, x], axis = 0)

    # results 정렬하기
    results = results.sort_values(['siteName'])

    results.to_csv('C:\\Users\\user\\jeju-dialect-translation\\csv_flie\\'+str(i+1)+".csv", sep=',', na_rep='NaN')

    results = pd.DataFrame(columns = {'siteName', 'contents'}) # 초기화
