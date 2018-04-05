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
            AdName = soup.find('span', class_='title-info-title-text').text.strip()
            #марка
            MarkAuto = soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[0].text.strip().split(' ')[1]
            #модель
            ModelAuto = soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[1].text.strip().split(' ')[1]
            #цена
            price = int(soup.find('div', class_='item-price').find('span', class_='price-value-string js-price-value-string').text.strip().split('\xa0₽')[0].replace(' ',''))

            #год выпуска
            YearOfIssue = int(soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[2].text.strip().split(' ')[2])
            #пробег
            Mileage = int(soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[3].text.strip().split(' ')[1].split('\xa0км')[0])
            #BodyType
            BodyType = soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[4].text.strip().split(' ')[2]
            #цвет
            Color = soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[5].text.strip().split(' ')[1]
            #Объём двигателя
            EngineCapacity = float(soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[6].text.strip().split(' ')[2].split('\xa0л')[0])
            #тип коробки передач
            TransmissionType = soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[8].text.strip().split(' ')[2]
            #привод
            DriveUnit = soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[10].text.strip().split(' ')[1]
            #Количество владельцев
            NumberOfOwners = int(soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[13].text.strip().split(' ')[3])
            #мощьность двигателя
            EnginePower = int(soup.find('ul', class_='item-params-list').find_all('li', class_="item-params-list-item")[15].text.strip().split(' ')[2].split('\xa0л.с.')[0])
            #описание
            Description = soup.find('div', class_='item-description-text').text.strip()
            #Изображение
            Picture ='https:' +  soup.find('div', class_='gallery-img-frame js-gallery-img-frame').get('data-url')
            #Циклическое получение картикок
            #Picture = 'https:' + soup.find('div', class_='gallery-imgs-container js-gallery-imgs-container').find_all('div', class_='gallery-img-frame js-gallery-img-frame')[1].get('data-url')


        except:
            continue
if __name__ == '__main__':
    main()
