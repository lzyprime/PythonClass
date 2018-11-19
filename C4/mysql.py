import pymysql

conInfo = {
    'host': '70a4c0a.all123.net',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'dlga'

}
conObj = pymysql.connect(**conInfo)
cursor = conObj.cursor

# 作业：
## 创建 商品表（学号姓名） ： （商品id pk）, 商品标识， 商品价格，商品链接
## --------------------------------->
## 查询数据 ， by （商品名称）， 商品 id

