import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from random import uniform



def get_total_pages(html):#получить количество страниц для парсинга
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='Paginator_paginator__1Ws9A').find('div').find_all('a',  class_='Paginator_button__u1e7D')[-1].get('href')
    total_pages = pages.split('=')[8]
    return int(total_pages)

def get_html(url, useragent=None, proxy=None): #получение html кода стрраницы в текстовом виде
    r = requests.get(url, headers=useragent, proxies=proxy)
    r.encoding = 'utf-8'
    return r.text

def get_links_from_page(html):#получение ссылок из всех объявлений на странице
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='app_gridContentChildren__17ZMX').find_all('a', class_="SerpSnippet_name__3F7Yu blackLink")
    f = open('someparsingresults/AmruLinks.txt', 'a')
    for ad in ads:
        try:
            link_on_auto = ad.get('href')
            f.write(link_on_auto + '\n')
        except:
            continue
    f.close()

def main():
    #https://am.ru/chel/search/?brandId=local&brandOrigin=1&photo=1&sellers=1&searchOrder=3&page=1
    useragents = open('hideparcing/useragents.txt').read().split('\n')
    proxies = open('hideparcing/proxies.txt').read().split('\n')

    base_url = 'https://am.ru/chel/search/?'
    page_part = 'page='
    query_part ='brandId=local&brandOrigin=1&photo=1&sellers=1&searchOrder=3&'

    url_gen = base_url + query_part
    useragent = {'User-Agent': choice(useragents)}
    proxy = {'http': 'http://' + choice(proxies)}
    total_pages = get_total_pages(get_html(url_gen, useragent, proxy))
    print('страниц на парсинг ' + str(total_pages))
    for i in range(1, total_pages + 1):
        sleep(uniform(2,7))
        coutExc = 0
        useragent = {'User-Agent': choice(useragents)}
        proxy = {'http': 'http://' + choice(proxies)}
        try:
            url_gen = base_url + query_part + page_part + str(i)
            html = get_html(url_gen, useragent, proxy)
            get_links_from_page(html)
            print('success')
        except:
            print('fail')
            coutExc+=1
            continue
    print('неотпарсено ' + str(coutExc))
if __name__ == '__main__':
    main()
