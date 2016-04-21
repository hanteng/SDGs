# -*- coding: utf-8 -*-
#歧視無邊，回頭是岸。鍵起鍵落，情真情幻。

import json

all=[u'targets', u'goals']
#dict_keys(['source', 'meta', 'targets'])
#dict_keys(['goals', 'source', 'meta'])

for x in all:
    # Reading data back
    with open('../{}.json'.format(x), 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Writing JSON data
    with open('en/{}.json'.format(x), 'w', encoding='utf-8') as f:
        json.dump(data, f)

for g in data["goals"]:
    print (g["topic"])
