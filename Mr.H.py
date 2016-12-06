#!/bin/python2.7
#coding=utf-8

# gamegrd@gmail.com
# gamegrd

import requests
import time
import random
import argparse

def vote(number):
    while number > 0:
        number = number -1
        try:
            rand=random.randrange(0x11111111,0xFEFEFEFE)
            headers = {'X-Forwarded-For': '%d.%d.%d.%d' % (rand >> 24 & 0xFF,rand >> 16 & 0xFF, rand >> 8 & 0xFF, rand & 0xFF  ) }
            print headers['X-Forwarded-For']
            payload = {'unitid': 'dd70fa55-e7e5-48dc-b56a-42c28a0bd53b'}
            r = requests.post("http://dasai.30edu.com.cn/Unit.SetVotes.data", data=payload,headers=headers)
            r=r.json()
            if False==r["status"]:
                print r["txt"]
            else:
                print r
            #print r["txt"]
            #time.sleep(1)
        except:
            pass
if '__main__' == __name__:
    parse=argparse.ArgumentParser()
    parse.add_argument("number",type=int,help="Number of votes")
    args=parse.parse_args()
    vote(args.number)

