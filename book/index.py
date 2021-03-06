import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from book.download import download_book_chapter

server = 'https://www.xsbiquge.com'


def main(url):
    req = requests.get(url)
    req.encoding = 'utf-8'
    html = BeautifulSoup(req.text, 'lxml')
    chapters = html.find('div', id='list').find_all('a')
    for chapter in tqdm(chapters):
        download_book_chapter(server + chapter.get('href'))


if __name__ == "__main__":
    main(
        server + '/15_15338'
    )
