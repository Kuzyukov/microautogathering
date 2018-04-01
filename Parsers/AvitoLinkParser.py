import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from random import uniform



def get_total_pages(html):#получить количество страниц для парсинга
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages clearfix').find_all('a',  class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)

def get_html(url, useragent=None, proxy=None): #получение html кода стрраницы в текстовом виде
    r = requests.get(url, headers=useragent, proxies=proxy)
    r.encoding = 'utf-8'
    return r.text

def get_links_from_page(html):#получение ссылок из всех объявлений на странице
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-main catalog_table').find_all('a', class_="item-description-title-link")
    f = open('someparsingresults/AvitoLinks.txt', 'a')
    for ad in ads:
        try:
            link_on_auto = ad.get('href')
            f.write('https://www.avito.ru' + link_on_auto + '\n')
        except:
            continue
    f.close()

def main():
    #'https://www.avito.ru/chelyabinsk/avtomobili/s_probegom/otechestvennie?s=104&user=1&i=1&p=2'
    useragents = open('hideparcing/useragents.txt').read().split('\n')
    proxies = open('hideparcing/proxies.txt').read().split('\n')

    base_url = 'https://www.avito.ru/chelyabinsk/avtomobili/s_probegom/otechestvennie?'
    page_part = 'p='
    query_part ='s=104&user=1&i=1&'

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
