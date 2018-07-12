from bs4 import BeautifulSoup
import requests
import csv
import string


def scrape():
    printable = set(string.printable)

    csv_file = open('news.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['NYTimes', 'WashingtonPost',
                         'CNN', 'FoxNews', 'WallStreet'])
    ny = [""]
    wp = [""]
    cn = [""]
    fn = [""]
    ws = [""]

    # New York Times #
    try:
        source = requests.get("https://www.nytimes.com/").text
        soup = BeautifulSoup(source, 'lxml')
        for article in soup.find_all('article'):
            for header in article.find_all('a'):
                if(header.text and 'Comments' not in header.text and '\n' not in header.text and len(header.text.split(" ")) > 4):
                    ny.append(filter(lambda x: x in printable, header.text))

    except (requests.ConnectionError):
        print ("ERROR. Invalid URL for NYTimes!")

    # Washington Post #
    try:
        source = requests.get(
            "https://www.washingtonpost.com/?noredirect=on").text
        soup = BeautifulSoup(source, 'lxml').find(
            'section', id='main-content')
        headlines = soup.find_all('div', class_='headline')
        for headline in headlines:
            if('\n' not in headline.a.text):
                wp.append(filter(lambda x: x in printable, headline.a.text))
    except (requests.ConnectionError):
        print ("ERROR. Invalid URL for WashingtonPost!")

    # Fox News #
    try:
        source = requests.get(
            "https://www.foxnews.com/").text
        soup = BeautifulSoup(source, 'lxml').find(
            'div', class_='main main-primary js-river')
        articles = soup.find_all('a')
        for a in articles:
            if a.text and len(a.text.split(" ")) > 3 and '\n' not in a.text:
                fn.append(filter(lambda x: x in printable, a.text))
    except (requests.ConnectionError):
        print ("ERROR. Invalid URL for WashingtonPost!")

    # Wall Street #
    try:
        source = requests.get(
            "https://www.wsj.com/").text
        soup = BeautifulSoup(source, 'lxml').find(
            'div', class_='cb-row')
        articles = soup.find_all('a')
        for a in articles:
            if a.text and len(a.text.split(" ")) > 3 and '\n' not in a.text:
                ws.append(filter(lambda x: x in printable, a.text))
    except (requests.ConnectionError):
        print ("ERROR. Invalid URL for WashingtonPost!")

    list = [len(ny), len(wp), len(cn), len(fn), len(ws)]
    size = max(list)
    for i in range(1, size):
        ny_article, wp_article, cn_article, fn_article, ws_article = "", "", "", "", ""
        if i < len(ny):
            ny_article = ny[i]
        if i < len(wp):
            wp_article = wp[i]
        if i < len(cn):
            cn_article = cn[i]
        if i < len(fn):
            fn_article = fn[i]
        if i < len(ws):
            ws_article = ws[i]
        csv_writer.writerow(
            [ny_article.encode("utf-8"), wp_article.encode("utf-8"), cn_article.encode("utf-8"), fn_article.encode("utf-8"), ws_article.encode("utf-8")])

    csv_file.close()


scrape()
