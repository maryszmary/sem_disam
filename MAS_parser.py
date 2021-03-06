
import re

class Word():
    """a dictionary entry"""
    def __init__(self, content):
        self.content = content
        self.name = self.extract_name()
        self.senses = self.get_senses()
        self.homonimous = len(self.senses) > 1
        self.notes = re.sub('\\[.+?\\]', '', 
            self.content.split('\n')[1].strip('\t'))

    def extract_name(self):
        name = self.content.split('\n', 1)[0]
        return re.sub('\\{\\[/?\'\\]\\}', '', name)

    def get_senses(self):
        res = ''.join(self.content.split('\n')[2:])
        res = res.replace('\t', '').replace(chr(9633), '')
        if '[b]2' in res:
            res = res.split('[b]2')
            return [re.sub('\\[.+?\\]', '', p) for p in res]
        return [re.sub('\\[.+?\\]', '', res)]

    def clean_content(self):
        res = ''.join(self.content.split('\n')[1:])
        res = self.content.replace('\t', '').replace(chr(9633), '')
        res = re.sub('\\[.+?\\]', '', res)
        return res
        

def data_extractor():
    with open('MAS.dsl', encoding='utf-16') as f:
        di = f.read()
    di = re.split('\\n\\t?\\n', di)
    di = [Word(entry) for entry in di if entry != '']
    return di


def get_adjs(di):
    return [w for w in di if w.name[-2:] in ['ый', 'ий', 'ой']]


words = data_extractor()
adjs = get_adjs(words)

print('adjective\t1_sense\t2_sense')
for adj in adjs:
    if adj.homonimous:
        print(adj.name + '\t' + adj.senses[0] + '\t' + adj.senses[1])
