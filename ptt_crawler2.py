#-*-coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib.parse
import requests
import tkinter
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from  matplotlib import cm
matplotlib.font_manager._rebuild()

def search(url, param) :
    res = requests.get(url, params=param)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def fetch_content(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    context = soup.select('.bbs-screen')[0].text
    return context

def plant_pie(percent, labels):
    colors = cm.rainbow(np.arange(len(percent))/len(percent))
    explode = (0.05, 0.05, 0.05)
    plt.pie(percent, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
    plt.legend(labels, loc=2)
    plt.axis('equal')
    plt.show()

string = ['帽子', '卡片', '手錶']
if __name__ == '__main__':
    num = []
    percent = []
    sum_all = 0
    domain = "https://www.ptt.cc"
    search_url = 'https://www.ptt.cc/bbs/Boy-Girl/search'
    find_param = {'q' : '生日'}
    html = search(search_url, find_param)
    titleDiv = html.select('.r-ent > div.title ')
    link = [ urllib.parse.urljoin( domain, item.select('a')[0].attrs['href'] ) for item in titleDiv]

    context = [fetch_content(url) for url in link]
    for sss in string:
        num.append(0)
    for sss in string:
        for ccc in context:
            num[string.index(sss)] += ccc.count(sss)
    # compute the sum
    for i in num :
        sum_all = sum_all + i
    # compute of percent
    for i in num :
        percent.append(round(i*100/sum_all))
    for i in range(len(string)):
        print('percent of ', string[i], ' is ', percent[i], '%')
    plant_pie(percent, string)