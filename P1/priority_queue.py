class priority_queue(object):
    def __init__(self, data=[], comp=lambda a, b: a < b):
        self.__data = []
        self.__comp = comp
        self.listToHeap(data)

    def __len__(self):
        return len(self.__data)

    def __leftChild(self, x):
        return (x << 1) + 1

    def __rightChild(self, x):
        return (x << 1) + 2

    def __father(self, x):
        return (x - 1) >> 1

    def __downAdjust(self, pos):
        l = self.__leftChild(pos)
        r = self.__rightChild(pos)
        if r < len(self.__data):
            if self.__comp(self.__data[pos], self.__data[l]) and not self.__comp(self.__data[l], self.__data[r]):
                self.__data[l], self.__data[pos] = self.__data[pos], self.__data[l]
                self.__downAdjust(l)
            elif self.__comp(self.__data[pos], self.__data[r]) and not self.__comp(self.__data[r], self.__data[l]):
                self.__data[r], self.__data[pos] = self.__data[pos], self.__data[r]
                self.__downAdjust(r)
        elif l < len(self.__data) and self.__comp(self.__data[pos], self.__data[l]):
            self.__data[l], self.__data[pos] = self.__data[pos], self.__data[l]
            self.__downAdjust(l)

    def __upAdjust(self, pos):
        if pos != 0:
            f = self.__father(pos)
            if self.__comp(self.__data[f], self.__data[pos]):
                self.__data[pos], self.__data[f] = self.__data[f], self.__data[pos]
                self.__upAdjust(f)

    def push(self, value):
        self.__data.append(value)
        self.__upAdjust(len(self.__data) - 1)

    def pop(self):
        if self.__data != []:
            self.__data[0], self.__data[-1] = self.__data[-1], self.__data[0]
            x = self.__data.pop()
            self.__downAdjust(0)
            return x

    def top(self):
        return self.__data[0]

    def empty(self):
        return self.__data == []

    def clear(self):
        self.__data = []

    def listToHeap(self, l):
        self.clear()
        self.__data = l
        for i in range(len(l) - 1, -1, -1):
            self.__downAdjust(i)

    def heapToList(self):
        return self.__data

## 测试类是否好用 ##

from random import randint

## 构造函数允许两个参数，list 和 比较规则， 默认为 [] 和 小于号规则大根堆
q = priority_queue()

for i in range(20):
    q.push(randint(0,100))
print(q.heapToList()) # tolist方法， 方便打印

print(q.top()) # 取顶

l = []
while not q.empty(): # 判空
    l.append(q.pop()) # 弹出顶，并返回顶值

print(l)