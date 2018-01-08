#from HEADER import *
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import re
dir = './chromedriver'
now = time.localtime()
s = "%04d%02d%02d_%02d시%02d분_추출" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)

if __name__ == "__main__":
    lastmodel = ''
    modeldata = []
    try:
        with open("LastLog.dat", 'r') as f:

            lastmodel = f.read()
        with open("TargetModel.txt", 'r') as f:
            for data in f.readlines()[int(lastmodel):]:
                modeldata.append(data.strip())
                # if lastmodel == data.strip():
                # print( data.strip())
    except:
        pass

    ID = input(">>> 아이디를 입력하세요::")
    PW = input(">>> 비밀번호를 입력하세요::")
    driver = webdriver.Chrome(dir)
    driver.get("https://login.aliexpress.com/buyer.htm?return=https%3A%2F%2Fwww.aliexpress.com%2F")
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="alibaba-login-box"]'))
    driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(ID)
    driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(PW)
    driver.find_element_by_xpath('//*[@id="fm-login-submit"]').click()
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="has-login-submit"]').click()
    except:
        pass
    lastidx = int(lastmodel)
    try:
        with open(s+".csv","w") as f:
            for model in modeldata:
            #while True:
                # 51 개 1page
                print("_"*20)
                #model = re.sub('[-=.#/?:$}\n]', '', input(">>> 모델을 입력하세요::"))
                print(">>> ",model, " parsing ...")
                titleList =[]
                shopList = []
                driver.get("https://www.aliexpress.com/premium/"+model+".html")
                time.sleep(2)
                html=driver.page_source
                #req = requests.get("https://www.aliexpress.com/premium/"+model+".html")
                #html = req.text
                #text를 객체로 변환
                soup = BeautifulSoup(html, 'html.parser')
                try:
                    driver.find_element_by_xpath('//*[@id="view-thum"]').click()
                except:
                    print("\t>>> 검색결과가 없습니다.")
                    continue
                html = driver.page_source
                # req = requests.get("https://www.aliexpress.com/premium/"+model+".html")
                # html = req.text
                # text를 객체로 변환
                soup = BeautifulSoup(html, 'html.parser')
                #총 몇개인지 가져오는 코드
                #try:
                result = int(re.sub('[-=.#/?:$,}\n]', '',soup.find('div',class_="search-result").find('strong').get_text()))
                print("\t>>> 총 ",result, "개 검색완료")
                Searchdivs = soup.findAll('div',attrs = {'class' : 'item'})
                #print(Searchdivs[11:])
                if result == (len(Searchdivs) - 3):
                    for Searchdiv in Searchdivs:
                        try:
                            titleList.append(Searchdiv.find('h3').get_text().strip())
                            shopList.append(Searchdiv.find('div',class_="store-name util-clearfix").get_text().strip())
                        except:
                            pass
                else:
                    i = 0
                    while True:
                        i = i + 1
                        driver.get("https://www.aliexpress.com/premium/" + model + ".html?page="+str(i))
                        time.sleep(2)
                        html = driver.page_source
                        # req = requests.get("https://www.aliexpress.com/premium/"+model+".html")
                        # html = req.text
                        # text를 객체로 변환
                        soup = BeautifulSoup(html, 'html.parser')
                        try:
                            driver.find_element_by_xpath('//*[@id="view-thum"]').click()
                        except:
                            break;
                        html = driver.page_source
                        # req = requests.get("https://www.aliexpress.com/premium/"+model+".html")
                        # html = req.text
                        # text를 객체로 변환
                        soup = BeautifulSoup(html, 'html.parser')
                        Searchdivs = soup.findAll('div', attrs={'class': 'item'})
                        print (len(Searchdivs))
                        for Searchdiv in Searchdivs:
                            try:
                                titleList.append(Searchdiv.find('h3').get_text().strip())
                                shopList.append(Searchdiv.find('div', class_="store-name util-clearfix").get_text().strip())
                            except:
                                pass
                print("\t>>> ", model, " parsing end ! ")
                for idx in range(0, len(titleList)):
                    f.write(model + ',')
                    f.write(titleList[idx] + ',')
                    f.write(shopList[idx] + '\n')
                lastidx += 1
        with open("LastLog.dat", 'w') as f: # 잘끝남
            f.write('0') # 0으로 초기화
    except:
        print("# 인터넷 접속 장애나, 알리 익스프레스 사이트로 프로그램 종료 ")
        print("# 다시시작하면 마지막꺼부터 다시 받아옵니다.")
        with open("LastLog.dat", 'w') as f: # 잘안끝남
            f.write(str(lastidx))

