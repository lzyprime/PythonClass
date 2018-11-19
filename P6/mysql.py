import pymysql

conInfo = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'PythonClass'

}
conObj = pymysql.connect(**conInfo)
cursor = conObj.cursor()

# 作业：
## 创建 商品表（学号姓名） ： （商品id pk）, 商品标识， 商品价格，商品链接
## --------------------------------->
## 查询数据 ， by （商品名称）， 商品 id

cursor.execute('''
    create table lzy617(
        productid INT primary key,
        productname text,
        productmark text,
        price DOUBLE,
        url text
    )
''')

cursor.execute('''
insert into lzy617 VALUES (1,'momei','39346110300',111.0,'https://detail.tmall.com/item.htm?id=39346110300&ali_trackid=2:mm_23460544_16314573_61008893:1542596379_202_1237655453&sku_properties=1627207:3232483')
''')

conObj.commit()

cursor.execute('''
select * from lzy617 where productname='momei'
''')
print(cursor.fetchall())

cursor.execute('''
select * from lzy617 where productid=1
''')
print(cursor.fetchall())
conObj.close()

## ((1, 'momei', '39346110300', 111.0, 'https://detail.tmall.com/item.htm?id=39346110300&ali_trackid=2:mm_23460544_16314573_61008893:1542596379_202_1237655453&sku_properties=1627207:3232483'),)
## ((1, 'momei', '39346110300', 111.0, 'https://detail.tmall.com/item.htm?id=39346110300&ali_trackid=2:mm_23460544_16314573_61008893:1542596379_202_1237655453&sku_properties=1627207:3232483'),)