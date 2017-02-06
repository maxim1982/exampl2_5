import codecs
import json

with codecs.open('newsfr.json', encoding="iso8859_5") as file_news:
    news = json.load(file_news)
#print(news)
for i in range(0, len(news['rss']['channel']['item'])):
    a = list((news['rss']['channel']['item'][i]['description']['__cdata']).split())
    #print('___N', i, type(a))
    print(a)
    for item in a:
        #print(item)

        if len(item) > 5:
            item = item.replace(',', '').replace(':', '').replace('!', '').replace('?', '').\
                replace('<br>', '').replace('/', '').split()
            # теперь не знаю как отобрать все топовые слова ... как проще ? в словать заносить как { слово : кол-во }?

            #print(', '.join([word for word in item if len(word) == len(sorted(item, key=len)[-1])]).lower())
            #print(item)
            pass

