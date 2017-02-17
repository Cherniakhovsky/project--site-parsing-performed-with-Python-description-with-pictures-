##отримаємо гілку сайту, як при верстці HTML,
##але тільки з текстовою інформацією (без тегів)
import re
import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response=urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup=BeautifulSoup(html, "html.parser")
    print(soup.get_text())
    
def main():
    f=open('2_IDEX (список найдених сайтів).txt')
    count=0
    for url in f:
        count+=1
        print (count,100*'*')
        print (url)

        print (100*'*',count,url)
        try:
            parse(get_html('http://'+url.strip()))
        except:
            print ('error',count,url)
            pass

if __name__=='__main__':
    main()
