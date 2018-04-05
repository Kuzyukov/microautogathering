import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from random import uniform


def get_html(url, useragent=None, proxy=None): #получение html кода стрраницы в текстовом виде
    r = requests.get(url, headers=useragent, proxies=proxy)
    r.encoding = 'utf-8'
    return r.text

def main():
    adLinks = useragents = open('someparsingresults/YoulaLinks.txt').read().split('\n')

    useragents = open('hideparcing/useragents.txt').read().split('\n')
    proxies = open('hideparcing/proxies.txt').read().split('\n')
    i=0
    for ad in adLinks:
        try:
            i+=1
            print(i)
            useragent = {'User-Agent': choice(useragents)}
            proxy = {'http': 'http://' + choice(proxies)}
            html = get_html(ad, useragent, proxy)
            soup = BeautifulSoup(html, 'lxml')
            #ссылка
            linkOnAd = ad
            #название
            AdName = soup.find('div', class_='AdvertCard_pageContent__24SCy app_pageBlock__19Uub').find('div', class_='AdvertCard_advertTitle__1S1Ak').text.strip()
            #марка
            MarkAuto= soup.find('div', class_='AdvertCard_pageContent__24SCy app_pageBlock__19Uub').find('div', class_='AdvertCard_advertTitle__1S1Ak').text.strip().split(' ')[0]
            #модель
            ModelAuto= soup.find('div', class_='AdvertCard_pageContent__24SCy app_pageBlock__19Uub').find('div', class_='AdvertCard_advertTitle__1S1Ak').text.strip().split(' ')[2]
            #год выпуска
            YearOfIssue =  int(soup.find('div', class_='AdvertCard_specs__2FEHc').find_all('div', class_="AdvertSpecs_data__xK2Qx")[0].text.strip())
            #цвет
            Color = soup.find('div', class_='AdvertCard_specs__2FEHc').find_all('div', class_="AdvertSpecs_data__xK2Qx")[6].text.strip()
            #пробег
            Mileage = int(soup.find('div', class_='AdvertCard_specs__2FEHc').find_all('div', class_="AdvertSpecs_data__xK2Qx")[1].text.strip().replace(' ','').replace('км',''))
            #цена
            price = int(soup.find('div', class_='AdvertCard_price__3dDCr AdvertCard_topAdvertHeaderCommon__2zUjb rouble').text.strip().replace(' ',''))

        except:
            continue
if __name__ == '__main__':
    main()
