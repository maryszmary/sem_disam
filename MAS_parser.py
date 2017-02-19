
import re

class Word():
    """docstring for Word"""
    def __init__(self, content):
        self.content = content
        self.name = self.extract_name()
        self.senses = self.get_senses()
        self.homonimous = len(self.senses) > 1

    def extract_name(self):
        name = self.content.split('\n', 1)[0]
        return re.sub('\\{\\[/?\'\\]\\}', '', name)

    def get_senses(self):
        if '[b]2' in self.content:
            print(self.content)
        return [self.content]
        

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
print(len(adjs))
hom = [adj for adj in adjs if '[b]1.' in adj.content]
bihom = [adj for adj in adjs if '[b]2.' in adj.content]
print(len(hom))
print(len(bihom))
diff = set(bihom).difference(set(hom))
print([el.content for el in diff])

# for adj in adjs:
#     if adj.name == 'важный':
#         print(adj.content)