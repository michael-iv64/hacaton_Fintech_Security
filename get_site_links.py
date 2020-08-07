from bs4 import BeautifulSoup 
from urllib.request import *
import re


regexp1 = r'^\w'# буквы + цифры + _  
regexp2 = r'^\D'# буквы + цифры + _  


import sys 

# ----- addres inspected site ---------------------

adr = 'spb.hh.ru'
i = 0

url = 'https://'+ adr
def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html


def main():
    opener = build_opener()
    opener.addheaders = [('User_Agent', 'Mozilla/5.0')]
    install_opener(opener)
    for i in range(1):
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')

        div = soup.find_all('a')
    links = []
    for a in div:
        link = a.get('href')
        links.append(link)
    print('links')
    print(links)
    print()

    
    links_unic = list(set(links))
    print()
    print('links_unic')
    print(links_unic)

# ----------------------------- запись ссылок в файл  ---------------------------------------
    with open(f'hacaton_security/complete/data/common_info/links/{adr}_links.txt', 'w', encoding='utf-8') as f:
        for line in links_unic:
            f.write(str(line) + ',')

main()


done = "Operation successfully completed"
print(done)

