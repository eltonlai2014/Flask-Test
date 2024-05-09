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
pyinstaller -F -c app.py -p db/__init__.py --hidden-import db --hidden-import sqlalchemy.sql.default_comparator --hidden-import sqlalchemy.ext.declarative --version-file=file_version_info.txt 
pyinstaller app.spec

    a.datas,
    [
        ("db/query.py", r"D:/Elton/TestArea/Flask-Test/db/query.py", "DATA"),
        ("db/main.py", r"D:/Elton/TestArea/Flask-Test/db/main.py", "DATA"),
        ("db/__init__.py", r"D:/Elton/TestArea/Flask-Test/db/__init__.py", "DATA"),
    ],


```
--add-data ".\\config\\*;.\\config"

pyinstaller -F run.py --hidden-import db --add-data ".\\ready;.\\ready" --add-data ".\\config;.\\config" --add-data ".\\app\\cert;.\\app\\cert" --add-data ".\\static;.\\static" --hidden-import config --hidden-import sqlalchemy.sql.default_comparator --hidden-import engineio.async_drivers.threading
pyinstaller run.spec
set DISK_FOLDER="D:\\Elton\\TestArea\\nsm-server - pack\\src\\web"


pyinstaller -F run.py --hidden-import db --add-data ".\\config\\*;.\\config" --add-data ".\\app\\cert\\*;.\\app\\cert" --hidden-import config --hidden-import sqlalchemy.sql.default_comparator --hidden-import engineio.async_drivers.threading