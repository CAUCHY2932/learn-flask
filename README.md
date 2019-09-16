# learn-flask

> 2019-08-27

learn flask for joy


## 如何运行

python enter.py即可



## 后期扩展

可能会教授api，以及网站相关内容


## 如何学习

flask官方文档，李辉以及狗书

## 文档结构

enter.py主文件

## 如何调试运行


win系统下

`set FLASK_APP=manage.py`

mac系统或linux下

`export FLASK_APP=manage.py`


首先运行`flask shell`，进入python终端

```python
from app import db
from app.models import Post, User

p1 = Post()
db.seesion.add(p1)
```


## 设定debug

FLASK_DEBUG = 1

不再支持app.run(debug=True)

## 初始化数据库

flask db init

flask db migrate

flask db upgrade

