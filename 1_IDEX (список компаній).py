#Здійснюємо імпорт компаній, які мають свій стенд на виставці IDEX
#(яка пройде в ОАЕ з 19.02.2017-23.02.2017)

from bs4 import BeautifulSoup
import requests
import re


for i in range(1,5):
    #для отримання всього списку компаній, потрібно вище замість "5" поставити "1000"
    url = 'http://www.idexuae.ae/exhibitors?&page='+str(i)+'&searchgroup=00000001-exhibitors'
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    for i in range(10):
        
      
          print (re.sub("^\s+|\n|\r|\s+$", '',soup.select('div div div ul li h2 a')[i].getText()))



