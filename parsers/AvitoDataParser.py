import requests
import psycopg2
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from random import uniform

connect = psycopg2.connect(database='postdb', user='postgressuser', host='localhost', password='password')
cursor = connect.cursor()

def get_html(url, useragent=None, proxy=None): #получение html кода стрраницы в текстовом виде
    r = requests.get(url, headers=useragent, proxies=proxy)
    r.encoding = 'utf-8'
    return r.text

def main():
    adLinks =  open('someparsingresults/AvitoLinks.txt').read().split('\n')

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
            try:
                AdName = soup.find('span', class_='title-info-title-text').text.strip()
            except:
                AdName = ''
                """
            #марка
            try:
                MarkAuto = soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[0].text.strip().split(' ')[1]
            except:
                MarkAuto = 1

            #модель
            try:
                ModelAuto = soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[1].text.strip().split(' ')[1]
            except:
                ModelAuto = 1
                """
            #цена
            try:
                Price = int(soup.find('div', class_='item-price').find('span', class_='price-value-string js-price-value-string').text.strip().split('\xa0₽')[0].replace(' ',''))
            except:
                Price = ''

            #год выпуска
            try:
                YearOfIssue = int(soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[2].text.strip().split(' ')[2])
            except:
                YearOfIssue = ''

            #пробег
            try:
                Mileage = int(soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[3].text.strip().split(' ')[1].split('\xa0км')[0])
            except:
                Mileage = ''
                """
            #BodyType
            try:
                BodyType = soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[4].text.strip().split(' ')[2]
            except:
                BodyType = 1

            #цвет
            try:
                Color = soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[5].text.strip().split(' ')[1]
            except:
                Color = 1
                """
            #Объём двигателя
            try:
                EngineCapacity = float(soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[6].text.strip().split(' ')[2].split('\xa0л')[0])
            except:
                EngineCapacity = ''
                """
            #тип коробки передач
            try:
                TransmissionType = soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[8].text.strip().split(' ')[2]
            except:
                continue

            #привод
            try:
                DriveUnit = soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[10].text.strip().split(' ')[1]
            except:
                continue
                """
            #Количество владельцев
            try:
                NumberOfOwners = int(soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[13].text.strip().split(' ')[3])
            except:
                NumberOfOwners = ''

            #мощьность двигателя
            try:
                EnginePower = int(soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[15].text.strip().split(' ')[2].split('\xa0л.с.')[0])
            except:
                EnginePower = ''
            #описание
            try:
                Description = soup.find('div', class_='item-description-text').text.strip()
            except:
                Description =''

            #Изображение
            try:
                Picture ='https:' +  soup.find('div', class_='gallery-img-frame js-gallery-img-frame').get('data-url')
            except:
                Picture = ''
            #Циклическое получение картикок
            #Picture = 'https:' + soup.find('div', class_='gallery-imgs-container js-gallery-imgs-container').find_all('div', class_='gallery-img-frame js-gallery-img-frame')[1].get('data-url')
            cursor.execute('INSERT INTO aggregation_avitoobject(linkOnAd, AdName, Price, YearOfIssue, Mileage, EngineCapacity, NumberOfOwners, EnginePower, Description, Picture) VALUES ('" + linkOnAd + "','" + AdName + "','" + Price + "','" + YearOfIssue + "','" + Mileage + "','" + EngineCapacity + "','" + NumberOfOwners + "','" + EnginePower + "','" + Description + "','" + Picture + "');')
            connect.commit()

        except:
            continue
connect.close()
if __name__ == '__main__':
    main()
