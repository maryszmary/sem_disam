
from nltk.corpus import stopwords
from pymystem3 import Mystem
import json
import string

FNAME = 'addition'
ADJ = 'полный'
STOPWORDS = stopwords.words('russian') + [ADJ, 'свой', 'кто-то', 'какой-то',
        'чей', 'твой', 'наш', 'ваш', 'это', 'который', 'чем']
NOISE = [' ' + el for el in list(string.punctuation) + list(string.digits)]\
    + [' %s ' % el for el in list(string.punctuation) + list(string.digits)]\
    + [el + ' ' for el in list(string.punctuation) + list(string.digits)]\
    + list(string.punctuation) + list(string.digits) + [' ', ' -- ', ' \n',
        '…', '», ', '\n', ', «', ' «', '» (', '« ', '...', '»']
m = Mystem()


def disambiuguate(bags):
    with open(FNAME, 'r', encoding='utf-8') as f:
        data = f.read().strip('\n').split('\n')
    f = open(FNAME + '.result.csv', 'w', encoding='utf-8')
    for line in data:
        context = m.lemmatize(line)
        context = clean_data(context)
        f.write(line + '\t' + get_meaning(context, bags) + '\n')
    f.close()
    return 0


def clean_data(words):
    return [w for w in words if w not in STOPWORDS and w not in NOISE]


def get_meaning(cont_bag, sense_bag):
    first_bag, sec_bag = sense_bag[0], sense_bag[1]
    first = sum([first_bag[word] for word in first_bag if word in cont_bag])
    second = sum([sec_bag[word] for word in sec_bag if word in cont_bag])
    if first == 0 and second == 0:
        return 'ZERO INTERSECTION'
    elif first > second:
        return 'First' # + str([word for word in first_bag if word in cont_bag]) + ' GIVING ' + str(first)
    else:
        return 'Second'


if __name__ == '__main__':
    with open('sense_bags.json', 'r', encoding='utf-8') as f:
        bags = json.load(f)
    disambiuguate(bags[ADJ])
