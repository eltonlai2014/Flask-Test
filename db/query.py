from main import create_session
from main import Test
from pprint import pprint
session = create_session()
print("-"*130)
# 查第一筆
result = session.query(Test).first()
pprint(result.__dict__)  # pprint 用於美化輸出

print("-"*130)
#查全部
result = session.query(Test).order_by(Test.publish_time.desc()).all()
for row in result:
    print(row.id, end=" ")
    print(row.title, end=" ")
    print(row.publish_time)
print("-"*130)

#條件查詢
result = session.query(Test).filter_by(id=3).first()
pprint(result.__dict__)
print("-"*130)

#分頁
result = session.query(Test).filter_by(category="創業補給站").offset(2).limit(5).all()
# 顯示取得幾筆
print(f"總共取得 {len(result)} 筆資料")
# 利用迴圈拜訪資料
for row in result:
    print(row.id, end=" ")
    print(row.title)
print("-"*130)

#update
try:
    datas = {"title": "測試", "content": "測試"}
    session.query(Test).filter_by(id=1).update(datas)
    session.commit()
except Exception as e:
    print(e.__class__.__name__)
    print(str(e))
finally:
    session.close()

session.close()