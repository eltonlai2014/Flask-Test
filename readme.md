# Install Flask
```
pip install -r .\flask.txt
``` 
# Upgrade pip
```
python.exe -m pip install --upgrade pip
```
# Pack python
```
pip install pyinstaller
pyinstaller -F app.py --hidden-import db --hidden-import sqlalchemy.sql.default_comparator --hidden-import sqlalchemy.ext.declarative
pyinstaller app.spec

    a.datas,
    [
        ("db/query.py", r"D:/Elton/TestArea/Flask-Test/db/query.py", "DATA"),
        ("db/main.py", r"D:/Elton/TestArea/Flask-Test/db/main.py", "DATA"),
    ],


```