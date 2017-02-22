
from nltk.corpus import stopwords
from pymystem3 import Mystem
import json
import re
import string

REPLACEMENTS = ['||', '---', '\\', 'Прил. к', '(устар.)', '(в 1 знач.)',
                'Прич. ', 'страд. ', 'прош. ', 'наст. ', 'сущ. '
                'в знач. ', 'прил. ', 'Биол.Прил. ', 'Лат. ', 'греч. ',
                'Превосх. ст. к ', 'кому-, чему-л. ', '…', 'Л. Толстой ',
                'И. Гончаров ', 'М. Горький ', 'и т. п.', '—\n', 'какому-л. ']
STOPWORDS = stopwords.words('russian') + ['Тургенев']
PUNC = string.punctuation
print(STOPWORDS)
m = Mystem()

def get_table():
    with open('hom.adj.csv', 'r', encoding='utf-8') as f:
        table = f.read().split('\n')[1:-1]
    table = [line.split('\t') for line in table if line != '']
    table = {en[0]: [vectorize(en[1]), vectorize(en[2])] for en in table}
    return table


def vectorize(context):
    context = clean(context)
    di = {}
    for word in context:
        word = word.strip(PUNC)
        if word:
            lemma = m.lemmatize(word)
            lemma = lemma[0]
            if lemma not in STOPWORDS:
                if lemma not in di:
                    di[lemma] = 1
                else:
                    di[lemma] += 1
    return di


def clean(text):
    text = re.sub('\\d\\.', '', text).lower()
    for el in REPLACEMENTS:
        text = text.replace(el, '')
    text = text.split()
    for el in string.whitespace:
        if el in text:
            text.remove(el)
    return text


if __name__ == '__main__':
    table = get_table()
    with open('sense_bags.json', 'w') as f:
        json.dump(table, f)
    print(table['мягкий'][0])
