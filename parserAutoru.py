import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from random import uniform
import csv


#https://auto.ru/cars/all/?image=true&sort_offers=cr_date-DESC&currency=RUR&output_type=list&page_num_offers=1"

def write_csv(data):#временное
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data['d'])

def get_html(url, useragent=None, proxy=None): #получение html кода стрраницы в текстовом виде
    r = requests.get(url, headers=useragent, proxies=proxy)
    r.encoding = 'utf-8'
    return r.text

def get_links_from_page(html):#получение ссылок из всех объявлений на странице
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('table', class_='listing-list listing listing-wrap__listing i-bem').find_all('a',  class_='link')
    for ad in ads:
        try:
            link_on_auto = ad.get('href')
            data = {'d':link_on_auto}
            write_csv(data)
        except:
            continue

def main():
    #url = 'https://auto.ru/cars/all/?image=true&sort_offers=cr_date-DESC&currency=RUR&output_type=list&dealer_org_type=4&page_num_offers=1'
    useragents = open('useragents.txt').read().split('\n')
    proxies = open('proxies.txt').read().split('\n')

    base_url = 'https://auto.ru/cars/all/?'
    page_part = 'page_num_offers='
    query_part ='image=true&sort_offers=cr_date-DESC&currency=RUR&output_type=list&dealer_org_type=4&'
    total_pages = 99

    for i in range(1, total_pages + 1):
        sleep(uniform(2,7))
        useragent = {'User-Agent': choice(useragents)}
        proxy = {'http': 'http://' + choice(proxies)}
        try:
            url_gen = base_url + query_part + page_part + str(i)
            html = get_html(url_gen, useragent, proxy)
            get_links_from_page(html)
            print('success')
        except:
            print('fail')
            continue

if __name__ == '__main__':
    main()
