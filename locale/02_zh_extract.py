# -*- coding: utf-8 -*-
#歧視無邊，回頭是岸。鍵起鍵落，情真情幻。

import docx
_from_lang="zh_Hans"
doc = docx.Document("../locale_src/N1528572.DOCX")

para_list=[]
SDG_begin=0
SDG_end=0

for i, para in enumerate(doc.paragraphs):
    if para.text.split()!=[]:
        #print ("{}>{}".format(i,para.text.split()[0])[:8])
        para_list.append((len(para_list), i, para.text.strip().split()[0][:8], para.text.strip()))
        if para.text.split()[0][:8]=='59.':
            SDG_begin = len(para_list)
        if para.text.split()[0][:8]=='17.19':
            SDG_end = len(para_list)-1

import csv
with open(_from_lang+'.csv', 'w', newline='', encoding='utf-8') as f:
    writer  = csv.writer (f)
    writer.writerows(para_list)

#Inbetween 59 and 60
targets_goals=dict()
for para in para_list[SDG_begin:SDG_end+1]:
    try:
        _id = para[2]
        _content = para[3].replace(para[2],"",1).strip()
        targets_goals[ _id ] = _content
        #print (_content)

    except:
        print(para[3])
     
        

import json
all=[u'targets', u'goals']
#dict_keys(['source', 'meta', 'targets'])
#dict_keys(['goals', 'source', 'meta'])

for x in all:
    # Reading data back
    with open('../{}.json'.format(x), 'r', encoding='utf-8') as f:
        data = json.load(f)
            
    # Assigning meta data  
    #data [ "meta" ] [ "description" ] = "Targets of the SDGs (Chinese)"
    data [ "source" ] = { "url": "http://www.un.org/ga/search/view_doc.asp?symbol=A/70/L.1&Lang=C",
                          "date": "18/09/2015"
                        }


    if x=="targets":
        for y in ['id']:
            items=[]
            for item in data[ x ]: #goals or targets
                _id = item[ "id" ]
                item[ "title" ] = targets_goals[_id]
                items.append(item)
            data[ x ]=items



    if x=="goals":
        for y in ['goal']:
            items=[]
            for item in data[ x ]: #goals or targets
                _id = item[ "goal" ]
                item[ "title" ] = targets_goals[ "目标{}.".format(_id)]
                items.append(item)
            data[ x ]=items

            


    # Writing JSON data
    with open('{}/{}.json'.format(_from_lang,x), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent="  ")

