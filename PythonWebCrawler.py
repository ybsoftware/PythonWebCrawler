#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
baseUrl = "https://www.biqukan.com/"
title = ""
def getHTMLText(url):
    try:
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        r = requests.get(url,timeout=30,headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
def getContent(url):
    r = getHTMLText(baseUrl + url) 
    soup=BeautifulSoup(r,'lxml')
    context = soup.find("div",class_="showtxt")
    return context.text
def main():
    r = getHTMLText(baseUrl+"45_45900/")
    soup=BeautifulSoup(r,'lxml')
    title = soup.title.text
    print(soup.title)
    fileName = title + ".txt";
    content = soup.find("meta",attrs={"name":"keywords"})
    print(content)
    urls = soup.find("dl").find_all(["dt","dd"])
    zwUrl = []
    zw = False
    for item in urls:
        if zw:
            detail = getContent(item.next.get("href"));
            detail = detail.replace("<br />","\r\n")
            # 打开一个文件
            fo = open(fileName, "a")
            fo.write(detail)
            fo.close    
            print item.next.get("href")
            print item.next
        if(item.name == "dt" and item.text.count("正文卷")):
            zw = True
if __name__ == "__main__":
    main()
