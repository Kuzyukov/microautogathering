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
    #url стрраницы которую необходимо отпасить
    url = 'https://auto.ru/cars/all/?image=true&sort_offers=cr_date-DESC&currency=RUR&output_type=list&dealer_org_type=4&page_num_offers=5'
    useragents = open('useragents.txt').read().split('\n')
    proxies = open('proxies.txt').read().split('\n')

    for i in range(10):#цикл для рандомизации useragents и проксей нужно ипользовать цикл из той програмы
        sleep(uniform(2,7))
        useragents = {'User-Agent': choice(useragents)}
        proxy = {'http': 'http://' + choice(proxies)}
        try:
            html = get_html(url, useragent, proxy)
        except:
            continue

if __name__ == '__main__':
    main()
