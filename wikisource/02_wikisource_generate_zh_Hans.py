# -*- coding: utf-8 -*-
#歧視無邊，回頭是岸。鍵起鍵落，情真情幻。

import json
import os

all=[u'targets', u'goals']
#dict_keys(['source', 'meta', 'targets'])
#dict_keys(['goals', 'source', 'meta'])

_from_lang = "zh_Hans"
directory = os.path.join("..","locale",_from_lang)

if not os.path.exists(directory):
    exit

HEADER='''
{{{{header
  | title = 可持续发展目标
  | author = | override_author=聯合國
  | section =   [[可持续发展目标|所有目標]]
  | previous =  [[可持续发展目标{_previous:s}]]
  | next =      [[可持续发展目标{_next:s}]] 
  | year = 2015
  | notes = 大会第六十九届会议提交关于通过2015年后发展议程的联合国首脑会议的决议草案
}}}}
'''

HEADING='''
<!-- {_topic:s}-->
==目标 {_num:d}. {_text:s}==
<!-- {_short:s}-->

'''

ITEM='''
{_num:s}  {_text:s}
'''

FOOTER='''
[[Category:可持续发展目标]]
{{PD-UN}}
'''


data={}
for x in all:
    # Reading data back
    with open('../locale/{}/{}.json'.format(_from_lang,x), 'r', encoding='utf-8') as f:
        data [x] = json.load(f)


for i in range(len(data['goals']['goals'])):#range(17):
    if i==0:
        _previous= '|所有目標'
    else:
        _previous= '/目标{num:d}|目标{num:d}'.format(num=i)

    if i==16:
        _next = '|所有目標'
    else:
        _next = '/目标{num:d}|目标{num:d}'.format(num=i+2)

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
    
