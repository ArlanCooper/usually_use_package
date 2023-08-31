sqlalchemy使用文档
===
[toc]


# 介绍
SQLAlchemy是Python中最有名的ORM工具。

**关于ORM**：

全称Object Relational Mapping（对象关系映射）。

特点是操纵Python对象而不是SQL查询，也就是在代码层面考虑的是对象，而不是SQL，体现的是一种程序化思维，这样使得Python程序更加简洁易读。

具体的实现方式是将数据库表转换为Python类，其中数据列作为属性，数据库操作作为方法。


**优点**：

简洁易读：将数据表抽象为对象（数据模型），更直观易读
可移植：封装了多种数据库引擎，面对多个数据库，操作基本一致，代码易维护
更安全：有效避免SQL注入

**为什么要用sqlalchemy?**

虽然性能稍稍不及原生SQL，但是操作数据库真的很方便！

## 概念和数据类型
- 概念

![img](../pics/database_pics/sqlalchemy01.jpg)

- 数据类型

![img](../pics/database_pics/sqlalchemy02.jpg)



# 使用
## 安装
```angular2html
pip install sqlalchemy
```
## 创建连接
```angular2html
from sqlalchemy import create_engine

engine = create_engine("mysql://user:password@hostname/dbname?charset=utf8")
```
备注：
create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
```angular2html
'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
```
你只需要根据需要替换掉用户名、口令等信息即可。

create_engine还有其它可选的参数，比如：
```angular2html
engine = create_engine("mysql://user:password@hostname/dbname?charset=utf8",
                       echo=True,
                       pool_size=8,
                       pool_recycle=60*30
                       )
1. echo: 当设置为True时会将orm语句转化为sql语句打印，一般debug的时候可用
2. pool_size: 连接池的大小，默认为5个，设置为0时表示连接无限制
3. pool_recycle: 设置时间以限制数据库多久没连接自动断开

```






# 参考文献
1. [Python笔记之SqlAlchemy使用](https://www.cnblogs.com/liu-yao/p/5342656.html)


