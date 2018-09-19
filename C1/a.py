# a = [1,2,3]
# b = [4,5,6]
# c = a + b
# d = a * 3
# print (c,'\n',d)

# a = (1,2,"7")
# b = ("44",'4',44)
# c = a + b
# d = a * 3
# print(c,'\n',d)
#
# a = ([1,2],5)
# # a[1] = 4
# a[0].append(3)
# print(a)

# l = [1,2,3]
# for i in l:
#     print(i)

# d = {
#     'k1' : 'v1',
#     'k2' : 'v2',
#     'k3' : 'v3'
# }
# if 'k1' in d:
#     print(d['k1'])
#     print(d.get('k1'))
#
# for i in d:
#     print(i , d[i])
#
# for i in d.items():
#     print(i)
#
# for x,y in d.items():
#     print(x,y)

s = set([1,2,3,4])
s2 = set([3,4,5,6])
print(s & s2)
print(s | s2)
print(s ^ s2)
print(s - s2)
print(s2 - s)
s.add(1)
s.add(23)
print(s)
s.remove(2)
s.pop()
print(s)