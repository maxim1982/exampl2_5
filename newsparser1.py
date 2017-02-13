import codecs
import json

with codecs.open('newsfr.json', encoding="iso8859_5") as file_news:
    news = json.load(file_news)

dict_word = {'слово': 0}
for i in range(0, len(news['rss']['channel']['item'])):
    list_word = list((news['rss']['channel']['item'][i]['description']['__cdata']).split())

    for x in list_word:
        if len(x) >= 6:
            #здесь хотелось убрать мусор ,но выдет ошибку если открыть:
            #  x = x.replace(',', '').replace('/', '').replace('"', '').replace('href=', '').replace(':', '').replace('!', '').replace('?', '').replace('<br>', '').split()

            # теперь в словать заносим как { слово : кол-во }
            if x in dict_word:
                dict_word[x] += 1
            else:
                dict_word[x] = 1

# счетчик - top
top = 0
for key in sorted(dict_word, key=dict_word.get, reverse=True):
    if top != 10:
        print(key, dict_word[key])
    else:
        break
    top += 1

