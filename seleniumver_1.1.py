#from HEADER import *
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import requests
import random
dir = './chromedriver'
now = time.localtime()
s = "%04d%02d%02d_%02d시%02d분_추출" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
isStart = True
try:
    bs4 = BeautifulSoup(requests.get("http://121.169.9.44/outsourcing/mrk001.php").text,'lxml')
    code = bs4.find('a').get_text()
    if code == '0':
        isStart = False
except:
    pass
if __name__ == "__main__":
    if isStart:
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
        IDlist =['khuphj@khu.ac.kr','pgh5986@gmail.com']
        PWlist =['g2820480','park0429']
        listidx = 0
        #chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--proxy-server=14.52.23.216:8080")
        #driver = webdriver.Chrome(executable_path=dir,chrome_options=chrome_options)
        driver = webdriver.Chrome(dir)
        driver.delete_all_cookies()
        #원랜 x
        driver.switch_to.window(driver.window_handles[0])

        driver.get('https://login.aliexpress.com/buyer.htm?spm=2114.11010108.1000002.7.269a3618mYyCzx&return=https%3A%2F%2Fwww.aliexpress.com%2F&random=398CAAA58595B2C1E2BD41BDE01B1F0'+str(random.randint(0,9)))
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="alibaba-login-box"]'))
        driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(IDlist[listidx])
        driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(PWlist[listidx])
        driver.find_element_by_xpath('//*[@id="fm-login-submit"]').click()
        time.sleep(2)
        try:
            driver.find_element_by_xpath('//*[@id="has-login-submit"]').click()
        except:
            pass
        lastidx = int(lastmodel)
        try:
            for model in modeldata:
                if listidx == 0:
                    driver.get('https://www.aliexpress.com/premium/test.html?d=y&blanktest=0&origin=y&smSign=GwAz8VxIFVoE4LkMM%2BjhgQ%3D%3D&tc=ppc&smToken=049556ffb8784473bf9fdaa09a2e33ec&initiative_id=SB_20180112165246&isViewCP=y&catId=0')
                time.sleep(0.5)
                try:
                    driver.find_element_by_xpath('/html/body/div[11]/div/div/a').click()
                except:
                    pass
                try:
                    driver.find_element_by_xpath('//*[@id="search-key"]').clear()
                    driver.find_element_by_xpath('//*[@id="search-key"]').send_keys(model)
                    driver.find_element_by_xpath('//*[@id="form-searchbar"]/div[1]/input').click()
                except:
                    driver.get('https://www.aliexpress.com/premium/'+model+'.html')

                # 51 개 1page
                print("_"*20)
                #model = re.sub('[-=.#/?:$}\n]', '', input(">>> 모델을 입력하세요::"))
                print(">>> ",model, " parsing ...")
                titleList =[]
                shopList = []
                time.sleep(3)
                html=driver.page_source
                #req = requests.get("https://www.aliexpress.com/premium/"+model+".html")
                #html = req.text
                #text를 객체로 변환
                soup = BeautifulSoup(html, 'html.parser')
                try:
                    driver.find_element_by_xpath('//*[@id="view-thum"]').click()
                except:
                    if 'captcha' in html:
                        while True:
                            listidx += 1
                            print("\t>>> 캡챠 발생 재시작")
                            driver.quit()
                            driver = webdriver.Chrome(dir)
                            driver.delete_all_cookies()
                            # 원랜 x
                            driver.switch_to.window(driver.window_handles[0])
                            driver.get('https://login.aliexpress.com/buyer.htm?spm=2114.11010108.1000002.7.269a3618mYyCzx&return=https%3A%2F%2Fwww.aliexpress.com%2F&random=398CAAA58595B2C1E2BD41BDE01B1F0'+str(random.randint(0,9)))
                            driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="alibaba-login-box"]'))
                            driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(IDlist[listidx%2])
                            driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(PWlist[listidx%2])
                            driver.find_element_by_xpath('//*[@id="fm-login-submit"]').click()
                            time.sleep(2)
                            try:
                                driver.find_element_by_xpath('//*[@id="has-login-submit"]').click()
                            except:
                                pass
                            driver.get('https://www.aliexpress.com/premium/test.html?d=y&blanktest=0&origin=y&smSign=GwAz8VxIFVoE4LkMM%2BjhgQ%3D%3D&tc=ppc&smToken=049556ffb8784473bf9fdaa09a2e33ec&initiative_id=SB_20180112165246&isViewCP=y&catId=0')
                            try:
                                driver.find_element_by_xpath('/html/body/div[11]/div/div/a').click()
                            except:
                                pass
                            try:
                                driver.find_element_by_xpath('//*[@id="search-key"]').clear()
                                driver.find_element_by_xpath('//*[@id="search-key"]').send_keys(model)
                                driver.find_element_by_xpath('//*[@id="form-searchbar"]/div[1]/input').click()
                            except:
                                driver.get('https://www.aliexpress.com/premium/' + model + '.html')
                            # 51 개 1page
                            print("_" * 20)
                            # model = re.sub('[-=.#/?:$}\n]', '', input(">>> 모델을 입력하세요::"))
                            print(">>> ", model, " parsing ...")
                            titleList = []
                            shopList = []
                            time.sleep(3)
                            html = driver.page_source
                            soup = BeautifulSoup(html, 'html.parser')
                            if 'captcha' in html:
                                print("\t>>> 2회이상 캡챠발생으로 몇초 이후에 다시 브라우저가 켜집니다")
                                time.sleep(random.randint(1,5))
                            else:
                                break
                        try:
                            driver.find_element_by_xpath('//*[@id="view-thum"]').click()
                        except:
                            lastidx += 1
                            print("\t>>> 검색결과가 없습니다.")
                            continue
                        result = int(re.sub('[-=.#/?:$,}\n]', '',
                                            soup.find('div', class_="search-result").find('strong').get_text()))
                        print("\t>>> 총 ", result, "개 검색완료")
                        Searchdivs = soup.findAll('div', attrs={'class': 'item'})
                        # print(Searchdivs[11:])
                        if result == (len(Searchdivs) - 3):
                            for Searchdiv in Searchdivs:
                                try:
                                    titleList.append(Searchdiv.find('h3').find('a')['title'].strip())
                                    shopList.append(
                                        Searchdiv.find('div', class_="store-name util-clearfix").get_text().strip())
                                except:
                                    pass
                        else:
                            i = 0
                            while True:
                                i = i + 1
                                driver.get("https://www.aliexpress.com/premium/" + model + ".html?page=" + str(i))
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
                                print(len(Searchdivs))
                                for Searchdiv in Searchdivs:
                                    try:
                                        titleList.append(Searchdiv.find('h3').find('a')['title'].strip())
                                        shopList.append(
                                            Searchdiv.find('div', class_="store-name util-clearfix").get_text().strip())
                                    except:
                                        pass
                        print("\t>>> ", model, " parsing end ! ")
                        with open(s + ".csv", "a") as f:
                            f.write(model + ',')
                            for idx in range(0, len(titleList)):
                                f.write(titleList[idx] + ',')
                                f.write(shopList[idx] + ',')
                            f.write('\n')
                        lastidx += 1
                        with open("LastLog.dat", 'w') as f:  # 잘끝남
                            f.write('0')  # 0으로 초기화
                    else:
                        print("\t>>> 검색결과가 없습니다.")
                        lastidx += 1
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
                            titleList.append(Searchdiv.find('h3').find('a')['title'].strip())
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
                                titleList.append(Searchdiv.find('h3').find('a')['title'].strip())
                                shopList.append(Searchdiv.find('div', class_="store-name util-clearfix").get_text().strip())
                            except:
                                pass
                print("\t>>> ", model, " parsing end ! ")
                with open(s + ".csv", "a") as f:
                    f.write(model + ',')
                    for idx in range(0, len(titleList)):
                        f.write(titleList[idx] + ',')
                        f.write(shopList[idx] + ',')
                    f.write('\n')
                lastidx += 1
            with open("LastLog.dat", 'w') as f: # 잘끝남
                f.write('0') # 0으로 초기화
        except:
            print("# 인터넷 접속 장애나, 알리 익스프레스 사이트로 프로그램 종료 ")
            print("# 다시시작하면 마지막꺼부터 다시 받아옵니다.")
            driver.quit()
            with open("LastLog.dat", 'w') as f: # 잘안끝남
                f.write(str(lastidx))
    else:
        print("컴퓨터를 최신버전으로 업그레이드하세요.")
        print("용량 부족이나 메모리 부족입니다.")
        print("크롬드라이버도 재설치후 재부팅하시고 다시 시도하세요 !")
        input()

