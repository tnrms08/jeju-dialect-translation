from django.shortcuts import render
# from django.http import HttpResponse

from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .forms import TransForm
from .models import Dictionary

import requests, bs4
import pandas as pd
from konlpy.tag import Hannanum, Okt
import re

import csv

# 다양한 방법이 있지만 CLASS 관리 진행

class Postview(View):
    def get(self, request):
        massage = "hello"
        return render(request, 'dialect/main_page.html',
                      {'msg': massage}
                      )

    @csrf_exempt

    def success(request):
        content = request.POST.get('content')

        dict = pd.read_csv("..\csv_flie\dictT.csv", sep=",", encoding='cp949')
        
        hannanum = Hannanum()
        okt = Okt()

        nouns = hannanum.nouns(content)
        stem = okt.morphs(content, stem = True)

        tmp=[]

        for i in range(0, len(stem)):
            if (len(stem[i]) == 1):
                tmp.append(stem[i])

        adjective = list(set(stem) - set(tmp))
        results = pd.DataFrame(columns = {'siteName', 'contents'})

        for i in nouns:
            x = dict[dict['siteName'] == i]
            x = x[['siteName', 'contents']]
            results = pd.concat([results, x], axis = 0)

        for i in adjective:
            y = dict[dict['siteName'].str.match(i)]
            results = pd.concat([results, y], axis = 0)

        temp = results.drop_duplicates()
        dic = temp.to_dict()

        han = re.compile('[가-힣\s]+')

        ex=[]
        
        for value in dic.items():
            x=str(value)
            value = han.findall(x)
            ex.append(value)

        k=ex[0]
        v=ex[1]

        space = {' '}

        k = [i for i in k if i not in space]
        v = [i for i in v if i not in space]

        result = { }

        for i in range(len(k)):
            result[k[i]]=v[i]
        

        return render(request, 'dialect/trans_suc.html',
                      { 'context': result}
                      )


    def dic(request):
        word = request.POST.get('dictionary')
        Word = {
            'word': word
        }
        return render(request, 'dialect/dictionary.html',
                      Word
                      )

lst = []

def dict_list0(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\dict3.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dictionary.html', {'lst': lst})
    
def dict_list1(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\1.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list1.html', {'lst': lst})

def dict_list2(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\2.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list2.html', {'lst': lst})

def dict_list3(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\3.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list3.html', {'lst': lst})

def dict_list4(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\4.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list4.html', {'lst': lst})

def dict_list5(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\5.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list5.html', {'lst': lst})

def dict_list6(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\6.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list6.html', {'lst': lst})

def dict_list7(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\7.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list7.html', {'lst': lst})

def dict_list8(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\8.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list8.html', {'lst': lst})

def dict_list9(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\9.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list9.html', {'lst': lst})

def dict_list10(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\10.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list10.html', {'lst': lst})

def dict_list11(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\11.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list11.html', {'lst': lst})

def dict_list12(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\12.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list12.html', {'lst': lst})

def dict_list13(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\13.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list13.html', {'lst': lst})

def dict_list14(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\14.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list14.html', {'lst': lst})

def dict_list15(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\15.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list15.html', {'lst': lst})

def dict_list16(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\16.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list16.html', {'lst': lst})

def dict_list17(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\17.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list17.html', {'lst': lst})

def dict_list18(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\18.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list18.html', {'lst': lst})

def dict_list19(request):
    lst = []
    path = 'C:\\Users\\user\\Documents\\jeju-dialect-translation\\csv_flie\\19.csv'
    file = open(path, 'r', encoding='UTF8')
    reader = csv.reader(file)
    print('-----', reader)
    for row in reader:
        lst.append(Dictionary(name=row[1],
                               contents=row[2]))
    lst = Dictionary.objects.bulk_create(lst)
    return render(request, 'dialect/dict_list19.html', {'lst': lst})