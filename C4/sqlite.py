import sqlite3

# conObj = sqlite3.connect(data:string, timeout?) 返回值为连接对象。具有事物特征
# cursor = conObj.cursor()  游标对象

## 操作开始 ##

# cursor.execute() # 执行语句. cursor.close() 关闭
# cursor.executemany() # (str, Iter) 占位符，动态数据做成可迭代
# cursor.executescript() # 脚本

# cursor.fetchxxx() 捕获返回值， xxx = all, many, one

# conObj.  rollback回滚 commit提交 close
# conObj.create_function() （名字， 参数个数， 函数），  自定函数


## 实例 ##
# 股票：date(日期), trans(交易类型), symbol(股票名称), qty(数量), price(股价)

stocks = sqlite3.connect('stocks.db')
cursor = stocks.cursor()


def doinsert():
    cursor.execute('''
    create table Stocks(
        date text,
        trans text,
        symbol text,
        qty real,
        price real
    )
    ''')

    cursor.execute(
        '''insert into Stocks Values('2018.11.14', 'BUY', 'Neusoft', 100, 1.2)''')

    stocks.commit()


if __name__ == "__main__":
    # doinsert()
    cursor.execute('''select * from Stocks''')
    print(cursor.fetchall())
    stocks.close()
