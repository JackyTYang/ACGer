import requests
import json
import os
from datetime import datetime
import re

# url = "http://10.214.241.121:9200/spec/_doc/"
# url = "http://localhost:9200/spec/_doc/"
# curr_url = "http://localhost:9200/_bulk/"
curr_url = "http://10.214.241.121:9200/_bulk/"
headers = {"Content-Type": "application/json"}
# toImport = ["anime", "book", "game", "music", "real_person", "character", "company"]
toImport = ["anime", "book", "game", "music"]

matchYear = re.compile('\d{1,4}[年/-]')
matchMonth = re.compile('[年/-]\d{1,2}[月/-]')
matchDay = re.compile('[月/-]\d{1,2}.{0,1}')
def parseDate(oriDateStr:str):
    match = matchYear.search(oriDateStr)
    if match is not None:
        year = oriDateStr[0:match.span()[1]-1]
    else:
        year = '1800'
    
    match = matchMonth.search(oriDateStr)
    if match is not None:
        month = oriDateStr[match.span()[0]+1 : match.span()[1]-1]
    else:
        month = '1'

    match = matchDay.search(oriDateStr)
    if match is not None:
        last = oriDateStr[match.span()[1] : match.span()[1]]
        if last.isdigit():
            day = oriDateStr[match.span()[0]+1 : match.span()[1]]
        else:
            day = oriDateStr[match.span()[0]+1 : match.span()[1]-1]
    else:
        day = '1'

    return year+'-'+month+'-'+day


for im in toImport:
    fpathlist = os.listdir(im)
    print(fpathlist)
    for fpath in fpathlist:
        with open("temp.json", "w", encoding="UTF-8") as tmpf:
            with open(im + "/" + fpath, "r", encoding="UTF-8") as fff:
                line = fff.readline()
                while line:
                    item = json.loads(line)
                    tmpf.write(
                        '{ "index":{"_index":"'
                        + im
                        + '","_id":"'
                        + str(item["guid"])
                        + '"}}\n'
                    )
                    
                    if item.__contains__('start_date'):
                        item['start_date'] = parseDate(item['start_date'])
                        tmpf.write(json.dumps(item, ensure_ascii=False))
                        tmpf.write("\n")
                    else:
                        tmpf.write(line)
                    
                    line = fff.readline()
            print("Write temp.json success")
        
        with open("temp.json", "r", encoding="UTF-8") as tmpf:
            body = tmpf.read()
            res = requests.post(url=curr_url, data=body.encode("utf-8"), headers=headers)
            print(res)

    # with open(im + "/detail(1).json", "r", encoding="UTF-8") as fff:
    #     for item in jsonlines.Reader(fff):
    #         # date_zh = item["start_date"]
    #         # if len(date_zh.split("年")) > 1:
    #         #     year = date_zh.split("年")[0]
    #         #     month = date_zh.split("年")[1].split("月")[0]
    #         #     day = date_zh.split("年")[1].split("月")[1].split("日")[0]
    #         #     item["start_date"] = year+"-"+month+"-"+day
    #         #     print(item["start_date"])
    #         req = curr_url + str(item["guid"])
    #         print(req)
    #         res = requests.put(url=req, json=item)
    #         print(res.status_code)
