import csv
from yattag import Doc


def read_file(filename):
    file = open(filename, mode="r")
    lines = csv.reader(file)
    dataset = []
    for row in lines:
        obj = {
            'title': str(row[0]),
            'logo': str(row[1]),
            'url': str(row[2]),
            'tags': row[3:len(row)-2],
            'statistics': str(row[len(row)-1].lstrip())
        }
        dataset.append(obj)
    file.close()
    return dataset


def build_html(dataset):
    doc, tag, text = Doc().tagtext()
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            doc.stag('meta', charset='utf-8')
            with tag('title'):
                text('Page')
            doc.stag('link', rel='stylesheet', href='style.css', type='text/css')
        with tag('body'):
            with tag('table'):
                with tag('tr'):
                    with tag('th'):
                        text('Site Logo')
                    with tag('th'):
                        text('URL')
                    with tag('th'):
                        text('Tags')
                    with tag('th'):
                        text('Statistics')
                for obj in dataset:
                    with tag('tr'):
                        with tag('td'):
                            doc.stag('img', src=obj['logo'], width=150, height=150, alt='Logo')
                        with tag('td'):
                            doc.stag('a', href=obj['url'], target='_blank')
                            text(obj['title'])
                        with tag('td'):
                            with tag('ul'):
                                for t in obj['tags']:
                                    with tag('li'):
                                        text(t)
                        with tag('td'):
                            text(obj['statistics'])
    return doc.getvalue()


def save_file(filename, data_to_write):
    file = open(filename, mode='w')
    file.write(data_to_write)
    file.close()


data = read_file('page.csv')
html = build_html(data)
save_file('index.html', html)
