# 文件操作

## 打开文件 open
### open(file:str,mode='rt', buffering = -1, encodeing = None) 文件地址,打开方式，缓冲区？编码格式

## 返回值： 文件类型的fobj, 若失败, 抛异常

## fObj.close

## 上下文管理语句 with open() as fObj:

### 写
str = "lsm "
with open(r'c3_1.md', mode="w") as fobj:
    fobj.write(str)

### 读
with open(r'c3_1.md', mode="r") as fr:
    print(fr.read(10))
    fr.seek(1)


#### seek() 光标偏移

## test

def lines(file):
    for line in file.readlines():
        yield line
    yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield block
            block = []


def tohtml(s):
    pass


with open(r'filetoRead.txt', mode='r') as fr:
    s = [x for x in blocks(fr)]
    print(s)
    tohtml(s)

## 二进制文件 pickle shelve 序列化，反序列化

i = 1000
a = 33.33
s = 'lsm'
lst = [1, 2, [3, 4]]
dic = {'a': '1', 'b': '2'}
tup = (i, a, s, lst, dic)
import pickle

with open(r's.bt', mode="wb") as fwb:
    pickle.dump(len(tup), fwb)
    for item in tup:
        pickle.dump(item, fwb)

with open(r's.bt', mode="rb") as frb:
    n = pickle.load(frb)
    for i in range(n):
        x = pickle.load(frb)
        print(type(x), x)

import shelve

d1 = {'age': 1, 'name': 'A', 'sex': 1}
d2 = {'age': 2, 'name': 'B', 'sex': 0}
with shelve.open(r'shelve.bt') as fp:
    fp['d1'] = d1
    fp['d2'] = d2

with shelve.open(r'shelve.bt') as fp:
    print(fp['d1'])
    print(fp['d2'])

### json
import json

jsonlst = json.dumps(lst)
print(jsonlst)
print(json.loads(jsonlst))

## 文件级操作

import os, os.path

l = [filename for filename in os.listdir('.') if filename.endswith(".bt")]

for f in l:
    os.rename(f, (f[:-3] + '.txt'))
