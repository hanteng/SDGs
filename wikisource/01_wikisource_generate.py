# -*- coding: utf-8 -*-
#歧視無邊，回頭是岸。鍵起鍵落，情真情幻。

import json
import os

all=[u'targets', u'goals']
#dict_keys(['source', 'meta', 'targets'])
#dict_keys(['goals', 'source', 'meta'])

_from_lang = "en"
directory = os.path.join("..","locale",_from_lang)

if not os.path.exists(directory):
    exit

HEADER='''
{{{{header
 | title      = Sustainable Development Goals
 | author     = | override_author=by the United Nations
 | translator = 
 | section    = 
 | previous   = [[Sustainable Development Goals{_previous:s}]]
 | next       = [[Sustainable Development Goals{_next:s}]] 
 | year       = 2015
 | portal     = Sustainable Development Goals
 | notes      = Adopted by the General Assembly on 25 September 2015
}}}}
'''

HEADING='''
<!-- {_topic:s}-->
==Goal {_num:d}. {_text:s}==
<!-- {_short:s}-->

'''

ITEM='''
{_num:s}  {_text:s}
'''

FOOTER='''
[[Category:Sustainable Development Goals]]
{{PD-UN}}
'''


data={}
for x in all:
    # Reading data back
    with open('../{}.json'.format(x), 'r', encoding='utf-8') as f:
        data [x] = json.load(f)


for i in range(len(data['goals']['goals'])):#range(17):
    if i==0:
        _previous= '|All goals'
    else:
        _previous= '/{num:d}|Goal {num:d}'.format(num=i)

    if i==16:
        _next = '|All goals'
    else:
        _next = '/{num:d}|Goal {num:d}'.format(num=i+2)

    #print (HEADER.format(_previous=_previous, _next=_next))

    ITEMS=''
    goal_num=i+1
    for target_item in list((d for d in data['targets']['targets'] if d['goal'] == goal_num)):
        ITEMS=ITEMS+ITEM.format( _num = target_item['id'],
                                 _text = target_item['title'])

    # Outputing text in wikipedia syntax


    output_text = HEADER.format (_previous=_previous, _next=_next) + \
                  HEADING.format(_num = data['goals']['goals'][i]['goal'], 
                                 _topic = data['goals']['goals'][i]['topic'], 
                                 _short = data['goals']['goals'][i]['short'], 
                                 _text = data['goals']['goals'][i]['title']  ).strip()  + ITEMS + FOOTER

    #print output_text

    _to_lang=_from_lang    
    with open('wiki_source_{}_{}.txt'.format(i+1, _to_lang), 'w', encoding='utf-8') as f:
        f.write(output_text)


'''
    # Writing JSON data
    with open('{}/{}.json'.format(_to_lang,x), 'w', encoding='utf-8') as f:
        json.dump(data, f)
'''
    
