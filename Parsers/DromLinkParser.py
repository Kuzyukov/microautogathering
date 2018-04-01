import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from random import uniform
"""
Добавить получение количества страниц
"""

def get_html(url, useragent=None, proxy=None): #получение html кода стрраницы в текстовом виде
    r = requests.get(url, headers=useragent, proxies=proxy)
    r.encoding = 'utf-8'
    return r.text

def get_links_from_page(html):#получение ссылок из всех объявлений на странице
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='b-media-cont b-media-cont_modifyMobile_sm').find_all('a', class_="b-advItem")
    f = open('DromLinks.txt', 'a')
    for ad in ads:
        if ad.get('class') == ['b-advItem']:
            try:
                link_on_auto = ad.get('href')
                f.write(link_on_auto + '\n')
            except:
                continue
    f.close()

def main():
    #'https://chelyabinsk.drom.ru/lada/page10/?ph=1&mileage_condition=2&go_search=2'
    useragents = open('useragents.txt').read().split('\n')
    proxies = open('proxies.txt').read().split('\n')

    base_url = 'https://chelyabinsk.drom.ru/'

    page_part = 'page'
    query_part ='/?ph=1&mileage_condition=2&go_search=2'

    total_pages = 90

    model_auto = 'lada/'
    for i in range(1, total_pages + 1):
        sleep(uniform(2,7))
        coutExc = 0
        useragent = {'User-Agent': choice(useragents)}
        proxy = {'http': 'http://' + choice(proxies)}
        try:
            url_gen = base_url + model_auto + page_part + str(i) + query_part
            html = get_html(url_gen, useragent, proxy)
            get_links_from_page(html)
            print('success')
        except:
            print('fail')
            coutExc+=1
            continue
    print('неотпарсено для ' + str(model_auto) + str(coutExc))

    model_auto = 'uaz/'
    total_pages = 5
    for i in range(1, total_pages + 1):
        sleep(uniform(2,7))
        coutExc = 0
        useragent = {'User-Agent': choice(useragents)}
        proxy = {'http': 'http://' + choice(proxies)}
        try:
            url_gen = base_url + model_auto + page_part + str(i) + query_part
            html = get_html(url_gen, useragent, proxy)
            get_links_from_page(html)
            print('success')
        except:
            print('fail')
            coutExc+=1
            continue
    print('неотпарсено для ' + str(model_auto) + str(coutExc))

    model_auto = 'gaz/'
    total_pages = 4
    for i in range(1, total_pages + 1):
        sleep(uniform(2,7))
        coutExc = 0
        useragent = {'User-Agent': choice(useragents)}
        proxy = {'http': 'http://' + choice(proxies)}
        try:
            url_gen = base_url + model_auto + page_part + str(i) + query_part
            html = get_html(url_gen, useragent, proxy)
            get_links_from_page(html)
            print('success')
        except:
            print('fail')
            coutExc+=1
            continue
    print('неотпарсено для ' + str(model_auto) + str(coutExc))

    model_auto = 'moskvitch/'
    total_pages = 1
    for i in range(1, total_pages + 1):
        sleep(uniform(2,7))
        coutExc = 0
        useragent = {'User-Agent': choice(useragents)}
        proxy = {'http': 'http://' + choice(proxies)}
        try:
            url_gen = base_url + model_auto + page_part + str(i) + query_part
            html = get_html(url_gen, useragent, proxy)
            get_links_from_page(html)
            print('success')
        except:
            print('fail')
            coutExc+=1
            continue
    print('неотпарсено для ' + str(model_auto) + str(coutExc))

if __name__ == '__main__':
    main()
