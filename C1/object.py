# var
## self.varname 随处定义 ， 成员
## Classname.varname 类属性

# self
## c++ : this-> , kotlin this.

# function
## 实例方法
## 类方法 : 修饰器 @classmethod， 第一个参数 cls
## 静态方法 @staticmethod

class Root:
    total = 0
    def __init__(self,v = 0):
        self.value = v
        Root.total += 1

    def show(self):
        print('value: ', self.value)
        print('total: ', Root.total)

    @classmethod
    def classShowTotal(cls):
        print('classmethod', cls.total)

    @staticmethod
    def staticShowTotal():
        print('staticmethod show : ',Root.total)

a = Root(5)
a.staticShowTotal()
a.classShowTotal()
a.show()

Root.show(a)
Root.staticShowTotal()
Root.classShowTotal()


# 访问限定 下划线
## __xxx__ 系统默认对象名
## __xxx : private
## _xxx : protected
## xxx : public

# class A:
#     def __init__(self):
#         self.__a = 1
#
# a = A
#
# print(a._A__a)

class Test:
    def __init__(self, v = 0):
        self.__value = v
        self.__value1 = v

    @property
    def value1(self):
        return self.__value1

    def __get(self):
        self.__value

    def __set(self, v):
        self.__value = v

    def __del(self):
        del self.__value

    value = property(__get, __set,__del)

t = Test(6)
print(t.value1)
print(t.value)
t.value = 2
print(t.value)
del t.value


class A:
    def __init__(self):
        print('A : ')


class B(A):
    def __init__(self):
        print('B : ')
        super().__init__()

class C(A):
    def __init__(self):
        print('C : ')
        super().__init__()

class D(B, C):
    def __init__(self):
        print('D : ')
        B.__init__(self)
        C.__init__(self)

d = D()

print(D.__mro__)