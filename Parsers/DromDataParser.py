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
    adLinks = useragents = open('someparsingresults/AmruLinks.txt').read().split('\n')

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
            #название
            title = soup.find('div', class_='AdvertCard_pageContent__24SCy app_pageBlock__19Uub').find('div', class_='AdvertCard_advertTitle__1S1Ak').text.strip()
            #модель
            #model= soup.find('div', class_='AdvertCard_pageContent__24SCy app_pageBlock__19Uub').find('div', class_='AdvertCard_advertTitle__1S1Ak').text.strip()
            #марка
            #mark= soup.find('div', class_='AdvertCard_pageContent__24SCy app_pageBlock__19Uub').find('div', class_='AdvertCard_advertTitle__1S1Ak').text.strip()
            #цена
            price = soup.find('div', class_='AdvertCard_pageContent__24SCy app_pageBlock__19Uub').find('div', class_='AdvertCard_price__3dDCr AdvertCard_topAdvertHeaderCommon__2zUjb rouble').text.strip()
            #год выпуска
            YearOfCarManufacture = soup.find('div', class_='AdvertCard_specs__2FEHc').find_all('div', class_="AdvertSpecs_data__xK2Qx")[0].text.strip()
            #пробег
            Mileage = soup.find('div', class_='AdvertCard_specs__2FEHc').find_all('div', class_="AdvertSpecs_data__xK2Qx")[1].text.strip()
            #кузов
            BodyType = soup.find('div', class_='AdvertCard_specs__2FEHc').find_all('div', class_="AdvertSpecs_data__xK2Qx")[2].text.strip()
            #коробка передач
            gearbox = soup.find('div', class_='AdvertCard_specs__2FEHc').find_all('div', class_="AdvertSpecs_data__xK2Qx")[3].text.strip()
            #Тип двигателя
            engine = soup.find('div', class_='AdvertCard_specs__2FEHc').find_all('div', class_="AdvertSpecs_data__xK2Qx")[4].text.strip()
            #Руль
            SteeringWheel = soup.find('div', class_='AdvertCard_specs__2FEHc').find_all('div', class_="AdvertSpecs_data__xK2Qx")[5].text.strip()
            #цвет
            Color = soup.find('div', class_='AdvertCard_specs__2FEHc').find_all('div', class_="AdvertSpecs_data__xK2Qx")[6].text.strip()
            #привод
            DriveUnit = soup.find('div', class_='AdvertCard_specs__2FEHc').find_all('div', class_="AdvertSpecs_data__xK2Qx")[7].text.strip()
            #мощность двигателя
            enginePower = soup.find('div', class_='AdvertCard_specs__2FEHc').find_all('div', class_="AdvertSpecs_data__xK2Qx")[8].text.strip()
            #количество владельцев
            Ownership = soup.find('div', class_='AdvertCard_specs__2FEHc').find_all('div', class_="AdvertSpecs_data__xK2Qx")[10].text.strip()

        except:
            continue
if __name__ == '__main__':
    main()
