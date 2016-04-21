# -*- coding: utf-8 -*-
#歧視無邊，回頭是岸。鍵起鍵落，情真情幻。

import json
_to_lang="pt"
import os

from translate import Translator
translator= Translator(to_lang=_to_lang)

all=[u'targets', u'goals']
#dict_keys(['source', 'meta', 'targets'])
#dict_keys(['goals', 'source', 'meta'])

directory=_to_lang
if not os.path.exists(directory):
    os.makedirs(directory)

def translate_c(c):
    #print (content)
    while True:
        print ("trying")
        try:
            translated = translator.translate(c)
        except:
            translated =""
            
        if "MYMEMORY WARNING" in translated:
            input ("Press Enter to continue...\n")
        else:
            break
    print("{}->{}".format(c[-15:], translated))
    return (translated)

for x in all:
    # Reading data back
    with open('../{}.json'.format(x), 'r', encoding='utf-8') as f:
        data = json.load(f)

    if x=="targets":
        for y in ['title']:
            items=[]
            for item in data[ x ]: #goals or targets
                content = item[ y ]
                item[ y ]=translate_c(content)
                items.append(item)
            data[ x ]=items

            
    if x=="goals":
        for y in ['topic', 'short', 'title']:
            items=[]
            for item in data[ x ]: #goals or targets
                content = item[ y ]
                #print (content)
                try:
                    translated = translator.translate(content)
                except:
                    translated =""
                item[ y ]=translated
                items.append(item)
            data[ x ]=items

            
    # Writing JSON data
    with open('{}/{}.json'.format(_to_lang,x), 'w', encoding='utf-8') as f:
        json.dump(data, f)

    

