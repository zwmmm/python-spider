import requests
from bs4 import BeautifulSoup


def chapter_format(text):
    return '\n'.join(text.strip().split('\xa0' * 4))


def download_book_chapter(link):
    resp = requests.get(url=link)
    resp.encoding = 'utf-8'
    html = resp.text
    bs = BeautifulSoup(html, 'lxml')

    # 提取标题和内容
    book_name = bs.find('title').text
    text = bs.find('div', id='content').text
    text = chapter_format(text)

    with open(book_name + '.txt', 'w') as file:
        file.write(text)


if __name__ == "__main__":
    # 测试章节下载
    download_book_chapter(
        'https://www.xsbiquge.com/15_15338/8549128.html'
    )
