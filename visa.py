import urllib.request
import time
import re
from bs4 import BeautifulSoup


URL = 'http://www.gofortravel.ru/usa/visa/application/our-help/latest-news#link66'


def get_html():
    raw_html = urllib.request.urlopen(URL).read().decode('utf-8')
    soup = BeautifulSoup(raw_html, "lxml")
    return soup


def get_comment_text(soup):
    comment_box = soup.find('div', class_='comments-list')
    # comment_body = comment_box.find_next('div', class_='comment-body')
    comment_body = comment_box.find('div', id='comment-body-22298')
    return comment_body


def find_match(comment_body):
    pattern = r'ВАЖНО|ЕКАТЕРИНБУРГ|Екатеринбкрг|Открыли запись'
    match = re.findall(pattern, str(comment_body))
    if 'Открыли запись' in match:
        good_message = 'В Екатеринбурге открыли запись на собеседование!'
        return good_message
    else:
        bad_message = 'Пока нет записи!'
        return bad_message


def visa_response():
    soup = get_html()
    comment_body = get_comment_text(soup)
    match = find_match(comment_body)
    return match

# while True:
    #     soup = get_html()
    #     comment_body = get_comment_text(soup)
    #     match = find_match(comment_body)
    #     print(match)
    #     time.sleep(10)


if __name__ == '__main__':
    result = visa_response()
    print(result)




