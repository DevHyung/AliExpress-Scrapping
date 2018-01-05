import requests
from bs4 import BeautifulSoup
import urllib.request
import re

if __name__ == "__main__":
    while True:
        # 51 개 1page
        model = re.sub('[-=.#/?:$}\n]', '', input(">>> 모델을 입력하세요::"))
        titleList =[]
        shopList = []
        req = requests.get("https://www.aliexpress.com/premium/"+model+".html")
        html = req.text
        #text를 객체로 변환
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.prettify())
        #총 몇개인지 가져오는 코드
        try:
            result = int(soup.find('div',class_="search-result").find('strong').get_text())
            Searchdivs = soup.findAll('div',attrs = {'class' : 'item'})
            for Searchdiv in Searchdivs:
                titleList.append(Searchdiv.find('h3').get_text().strip())
                shopList.append(Searchdiv.find('div',class_="store-name util-clearfix").get_text().strip())
            with open(model+".csv",'w') as f:
                for idx in range(0,len(titleList)):
                    f.write(model+',')
                    f.write(titleList[idx] + ',')
                    f.write(shopList[idx] + '\n')
        except:
            print (">>> ",model, "의 검색결과가 없습니다.")
