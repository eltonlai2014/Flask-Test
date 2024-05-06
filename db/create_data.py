from main import create_session
from main import Test
import json
from datetime import datetime

import os

# Opening JSON file
f = open(os.path.abspath(os.getcwd())+'\\db\\data.json',encoding='utf-8')
 
# returns JSON object as 
# a dictionary
datas = json.load(f)
 
# Iterating through the json
# list
session = create_session()
for item in datas:
    data_obj = {
        "title": item["標題"],
        "content": item["內容"],
        "picture": item["主圖"],
        "category": item["分類"],
        "youtube": item["youtube嵌入代碼"],
        "slideshare": item["slideshare嵌入代碼"],
        "publish_time": datetime.strptime(item["建立時間"], "%Y%m%d%H%M%S"),
        "update_time": datetime.strptime(item["修改時間"], "%Y%m%d%H%M%S")
    }
    session.add(Test(**data_obj))
session.commit()
session.close()


# Closing file
f.close()    