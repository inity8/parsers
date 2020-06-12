import requests
import csv
from multiprocessing import Pool


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('websites.csv', 'a') as file:
        order = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


def get_page_data(text):
        data = text.strip().split('\n')[1:]
        for row in data:
            colums = row.strip().split('\t')
            name = colums[0]
            url = colums[1]
            description = colums[2]
            traffic = colums[3]
            percent = colums[4]

            data = {'name': name,
                    'url': url,
                    'description': description,
                    'traffic': traffic,
                    'percent': percent}
            write_csv(data)


def make_all(url):
    text = get_html(url)
    get_page_data(text)


def main():
    #7866
    url = 'https://www.liveinternet.ru/rating///today.tsv?page={}'
    urls = [url.format(str(i)) for i in range(1, 7867)]

    with Pool(20) as p:
        p.map(make_all, urls)


if __name__ == '__main__':
    main()

