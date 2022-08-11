from selenium import webdriver
from bs4 import BeautifulSoup as soup
import re, contextlib
import time
import pandas as pd
import numpy
import csv

textScrapped=[]
def webScrap(d,url,machista):
   d.get(url)
   time.sleep(1)
   while True:
      try:
         d.find_element("xpath","//*[@id=\"sd-cmp\"]/div[2]/div/div/div/div/div/div/div[2]/div[1]/button[1]/span").click()
      except:
         print("cookies aceptadas")
      try:
         for x in soup(d.page_source, 'html.parser').find_all("div",{"style":"word-wrap:break-word;"}):
            text=''.join(list(filter(None,map(lambda x: x.strip().replace(";",",").replace("\"","").replace("\n"," "),x.find_all(text=True, recursive=False)))))
            if(text!=''):
               textScrapped.append([text,('1' if machista else '0')])
            
            

         button=d.find_element("xpath","/html/body/div[3]/div/div/table[5]/tbody/tr/td[2]/div/table/tbody/tr/td[last() - 1]/a")
         if 'smallfont' in button.get_attribute('class').split():
            button.click()
         else:
            break;
      except:
         break
##50 machistas, 51-245 solteros +45, chica 246-334,Niña comentario 335-511,cambio climatico 512-796
urlMachistas=['https://forocoches.com/foro/showthread.php?t=9185801','https://forocoches.com/foro/showthread.php?t=9185825','https://forocoches.com/foro/showthread.php?t=9177237']
urlNormales=['https://forocoches.com/foro/showthread.php?t=9184893','https://forocoches.com/foro/showthread.php?t=9185805','https://forocoches.com/foro/showthread.php?t=9182999']
d = webdriver.Chrome('C://Users/Bc/Desktop/tfm/chromedriver.exe')

for x in urlMachistas:
   webScrap(d,x,True)
#for x in urlNormales:
 #  webScrap(d,x,False)

with open("dataset.csv","w+",encoding="utf-8", newline='') as my_csv:
    newarray = csv.writer(my_csv,delimiter=';')
    newarray.writerows(textScrapped)
d.close()