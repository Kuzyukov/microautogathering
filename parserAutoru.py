import requests
from bs4 import BeautifulSoup
#https://auto.ru/cars/all/?image=true&sort_offers=cr_date-DESC&currency=RUR&output_type=list&page_num_offers=5"
def get_html(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text
def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pager__wrap').find_all('label',  class_='radio')[-1]
    total_pages = pages.find('input', class_='radio__control').get('value')
    return int(total_pages)

def get_links_from_page(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('table', class_='listing-list listing listing-wrap__listing i-bem').find_all('a',  class_='link')
    for ad in ads:
        try:
            link_on_auto = ad.get('href')
        except:
            link_on_auto =''
#[-1].get('href')
def main():
    url = 'https://auto.ru/cars/all/?image=true&sort_offers=cr_date-DESC&currency=RUR&output_type=list&dealer_org_type=4&page_num_offers=5'
    base_url = 'https://auto.ru/cars/all/?'
    page_part = 'page_num_offers='
    query_part ='image=true&sort_offers=cr_date-DESC&currency=RUR&output_type=list&dealer_org_type=4&'
    total_pages = get_total_pages(get_html(url))
    for i in range(1, 1 + 1):
        url_gen = base_url + query_part + page_part + str(i)
        #print(url_gen)
        html = get_html(url_gen)
        print(html)
        get_links_from_page(html)


if __name__ == '__main__':
    main()
