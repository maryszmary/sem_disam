
import re
import string

REPLACEMENTS = ['||', '---', '\\', 'Прил. к', '(устар.)', '(в 1 знач.)',
                'Прич. ', 'страд. ', 'прош. ', 'наст. ', 'сущ. '
                'в знач. ', 'прил. ', 'Биол.Прил. ', 'Лат. ', 'греч. ',
                'Превосх. ст. к ', 'кому-, чему-л. ']
STOP_WORDS = ['и', 'в', 'к', 'о', 'не']

def get_table():
	with open('hom.adj.csv', 'r'. 'utf-8') as f:
		table = f.read().split('\n')[1:]
	table = {en[0]: [vectorize(en[1]), vectorize(en[2])] for en in table}
	return table

def vectorize(context):
	context = clean(context)


def clean(text):
	text = re.sub('\\d\\.', '', text)
	for el in REPLACEMENTS:
		text = text.replace(el, '')
	return text
