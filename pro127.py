from bs4 import BeautifulSoup
from selenium import webdriver 
import time,csv 
url= 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('chromedriver.exe')
browser.get(url)
time.sleep(10)
def scrape():
    header=['name','distance','mass','radius']
    Data=[]
    for i in range(0,2):
        soup=BeautifulSoup(browser.page_source,'html.parser')
        for tag  in soup.find_all('ul',attrs={'class','star'}):
            litags=tag.find_all('li')
            tempList=[]
            for index,li in enumerate(litags):
                if index == 0 :
                    tempList.append(li.find_all('a')[0].contents[0])
                else:
                    try:
                        tempList.append(li.contents[0])
                    except:
                        tempList.append('')   
            Data.append(tempList)
        browser.find_element_by_xpath ('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()                

                
        


    with open ('star.csv','w') as f:
        cw=csv.writer(f)
        cw.writerow(header)
        cw.writerows(Data)

scrape()