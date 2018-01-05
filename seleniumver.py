import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import re
dir = './chromedriver'
ID = "parkhungjoon@naver.com"
PW = "g2820480"
if __name__ == "__main__":
    driver = webdriver.Chrome(dir)
    driver.get("https://login.aliexpress.com/")
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="alibaba-login-box"]'))
    driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(ID)
    driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(PW)
    driver.find_element_by_xpath('//*[@id="fm-login-submit"]').click()
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="has-login-submit"]').click()
    except:
        pass
    while True:
        # 51 개 1page
        model = re.sub('[-=.#/?:$}\n]', '', input(">>> 모델을 입력하세요::"))
        titleList =[]
        shopList = []
        driver.get("https://www.aliexpress.com/premium/"+model+".html")
        time.sleep(5)
        html=driver.page_source
        #req = requests.get("https://www.aliexpress.com/premium/"+model+".html")
        #html = req.text
        #text를 객체로 변환
        soup = BeautifulSoup(html, 'html.parser')
        #총 몇개인지 가져오는 코드
        #try:
        result = int(soup.find('div',class_="search-result").find('strong').get_text())
        print(result)
        Searchdivs = soup.findAll('div',attrs = {'class' : 'item'})
        print(Searchdivs[11:])
        for Searchdiv in Searchdivs:
            try:
                titleList.append(Searchdiv.find('h3').get_text().strip())
                shopList.append(Searchdiv.find('div',class_="store-name util-clearfix").get_text().strip())
            except:
                pass
        with open(model+".csv",'w') as f:
            for idx in range(0,len(titleList)):
                f.write(model+',')
                f.write(titleList[idx] + ',')
                f.write(shopList[idx] + '\n')
        #except:
         #   print (">>> ",model, "의 검색결과가 없습니다.")
