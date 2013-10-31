import sys
import time
import json
import requests
from bs4 import BeautifulSoup

def get_param(argv):
    #no options provide
    if len(argv) < 2:
        print('You must provide a username : ')
        print('usage: {0} username'.format(sys.argv[0]))
        sys.exit()
    return str(argv[1])

def get_urls_list(user_name, categories_keys, sub_categories_keys):
    '''
        :return: dict of formated url to parse. Example :
        {
            "films": {
                "Wish": "/user_name/collection/wish/films",
                "rating": "/user_name/collection/rating/films",
                "shopping": "/user_name/collection/shopping/films"
            }
        }
    '''
    urls_list = {}
    for c in categories_keys:
        url = []
        for sc in sub_categories_keys:
            url.append((sc, '/{0}/collection/{1}/{2}'.format(user_name, sc, c)))
        #dict([('A', 1), ('B', 2)]) => {'A': 1, 'B': 2}
        urls_list[c] = dict(url)
    return urls_list

#list item generator
def get_item(bs_item):
    items = bs_item.find_all('li')
    empty = bs_item.find('li', class_='d-emptyMessage')
    if items is None or empty:
        items = []
    yield from items #http://docs.python.org/3/whatsnew/3.3.html#pep-380

def get_original_title(bs_item):
    span = bs_item.find('span', 'elco-original-title')
    if span is not None:
        return str(span.string.strip())
    return ''

def get_title(bs_item):
    h2 = bs_item.find('h2', 'elco-title')
    if h2 is not None:
        if h2.a is not None:
            return str(h2.a.string.strip())
    return ''

def extract_date(bs_item):
    wrapper = bs_item.find('span', 'elco-date')
    if wrapper is not None:
        return wrapper.string[1:5]
    return ''

def get_authors(bs_item):
    wrapper = bs_item.find('p', 'elco-baseline')
    if wrapper is not None:
        links = wrapper.find_all('a')
        #return [str(string) for a in links for string in a.stripped_strings]
        return [str(a.string.strip()) for a in links]
    return []

def get_next_page(bs_item):
    pagination_item = bs_item.find('ul', 'eipa-pages')
    if pagination_item is not None:
        active_item = pagination_item.find('span', 'eipa-current').parent
        next_item = active_item.find_next_sibling('li')
        if next_item is not None:
            return next_item.find('a').get('href')
    return None

def get_page_content(url):
    try:
        r = requests.get(url)
    #TODO : better exceptions
    except requests.exceptions.InvalidSchema as e:
        sys.exit(e)
    return BeautifulSoup(r.content, 'html5lib')

def get_and_format_data(bs_item, data_collection, keys):
    list_item = bs_item.find('ul', 'elco-collection-list')
    if list_item is not None:
        li_items = get_item(list_item)
        for li in li_items:
            datas = []
            datas.append(get_title(li))
            datas.append(get_original_title(li))
            datas.append(get_authors(li))
            datas.append(extract_date(li))
            data_collection.append(dict(zip(keys, datas)))

def main():
    json_keys = ('title', 'original_title', 'authors', 'year')
    base_url = 'http://www.senscritique.com'
    char_encoding = 'UTF-8'
    categories = ('films', 'bd', 'series', 'jeuxvideo', 'musique')
    sub_categories = ('wish', 'rating', 'shopping')

    user  = get_param(sys.argv)
    urls  = get_urls_list(user, categories, sub_categories)
    collection = {}

    for category in categories:
        collection[category] = {}
        sub_cat = urls[category]
        for k, v in sub_cat.items():
            collection[category][k] = []
            page_url = v
            while page_url:
                time.sleep(1)
                content = get_page_content(base_url+page_url)
                get_and_format_data(content, collection[category][k], json_keys)
                page_url = get_next_page(content)
    with open('sc-collection.json', 'w', encoding = char_encoding) as output:
        output.write(json.dumps(collection))

if __name__ == '__main__':
    main()
