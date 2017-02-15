import codecs
import json

dict_word = {'слово': 0}


def read_news(file, codepage):
    print('read: ', file)
    with codecs.open(file, encoding=codepage) as file_news:
       news = json.load(file_news)

    for i in range(0, len(news['rss']['channel']['item'])):
        list_word = list((news['rss']['channel']['item'][i]['description']['__cdata']).split())

        for x in list_word:
            x = x.replace(',', '').replace('/', '').replace('"', '').replace('href=', '').replace(':', '')\
                .replace('!', '').replace('?', '').replace('<br>', '')
            if len(x) >= 6:
                # теперь в словать заносим как { слово : кол-во }
                if x in dict_word:
                    dict_word[x] += 1
                else:
                    dict_word[x] = 1


def read_news_2(file, codepage):
    print('read: ', file)
    with codecs.open(file, encoding=codepage) as file_news:
       news = json.load(file_news)

    for i in range(0, len(news['rss']['channel']['item'])):
        list_word = list((news['rss']['channel']['item'][i]['description']).split())

        for x in list_word:
            x = x.replace(',', '').replace('/', '').replace('"', '').replace('href=', '').replace(':', '')\
                .replace('!', '').replace('?', '').replace('<br>', '')
            if len(x) >= 6:
                # теперь в словать заносим как { слово : кол-во }
                if x in dict_word:
                    dict_word[x] += 1
                else:
                    dict_word[x] = 1

read_news('newsfr.json', 'iso8859_5')
read_news('newsafr.json', 'utf-8')
read_news('newscy.json', 'koi8-r')
read_news_2('newsit.json', 'cp1251')

# счетчик - top
top = 0
for key in sorted(dict_word, key=dict_word.get, reverse=True):
    if top != 10:
        print(key, dict_word[key])
    else:
        break
    top += 1

