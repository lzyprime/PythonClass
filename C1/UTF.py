# 字符编码
# ASCII UTF-8 UTF-16

b = 'abc'.encode(encoding='GBK') # type(b) ==== bytes
# string

## 格式化

print("{0}, {0:o}, {1:#x}".format(666,2222))

print("{name}, {age}".format(name = 'aaa', age = '100'))

s = '2018-10-10'

print(s.split('-'))

print(s.partition('-'))

print(s.rpartition('-'))

print(s.join('abc'))

print(','.join(s))

import string

before = string.ascii_letters

low = string.ascii_lowercase
up = string.ascii_uppercase

k = 2

after = low[k:] + low[:k] + up[k:] + up[:k]

table = ''.maketrans(before,after)

s = 'asdf'
print(s.translate(table))

s = '1122334'
print(s.replace('4', '44'))

print(s.find('2'))
print(s.rfind('2'))
print(s.find('5'))
print(s.index('2'))
# print(s.index('5'))

print(s.count('2'))