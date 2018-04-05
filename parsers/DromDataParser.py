import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from random import uniform


def get_html(url, useragent=None, proxy=None): #получение html кода стрраницы в текстовом виде
    r = requests.get(url, headers=useragent, proxies=proxy)
    r.encoding = 'windows-1251'
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
            #ссылка
            linkOnAd = ad
            #Название
            AdName = soup.find_all('div', class_='b-flex__item')[1].find_all('h3', class_='b-title b-title_type_h3')[0].text.strip()
            #марка
            MarkAuto= soup.find('div', class_='b-left-side').find('h1').text.strip().split(' ')[1]
            #модель
            ModelAuto = soup.find('div', class_='b-left-side').find('h1').text.strip().split(' ')[2]
            #год выпуска
            YearOfIssue = int(soup.find_all('div', class_='b-flex__item')[1].find_all('h3', class_='b-title b-title_type_h3')[0].text.strip().split(' ')[2])
            #Цвет 26
            Color = soup.find('div', class_='b-media-cont b-media-cont_relative').text.strip().replace('\n','').split(' ')[25].replace('Пробег','')
            #пробег
            Mileage = int(soup.find('div', class_='b-media-cont b-media-cont_relative').text.strip().replace('\n','').split(' ')[30].replace('Поколение:',''))
            #Цена
            price = int(soup.find('div', class_='b-media-cont b-media-cont_theme_dot').text.strip().replace('\xa0','').replace('q',''))
        except:
            continue
if __name__ == '__main__':
    main()
