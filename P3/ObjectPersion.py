# 作业:
# 定义一个人类（Person）
# 属性包括:姓名，性别，年龄，ID，
# 行为：吃，睡，工作
# 定义一个学生子类继承人类（Student）
# 增加属性：学校，学号
# 行为：重写工作方法（学习）
# 定义一个员工子类继承人类（Worker）
# 增加属性：公司名称，技术方向，工作年限
# 行为：重写工作方法（写代码）

# 实例化员工对象，要统计该类一共已经有了多少员工对象

# 编写测试函数，对上述实现进行测试

class Person:
    def __init__(self, name, sex, age, ID):
        self.name = name
        self.sex = sex
        self.age = age
        self.ID = ID

    def eat(self, something):
        print (self.name, ' eat ', something)

    def sleep(self, time = 6.0):
        if time < 0:
            time = 6.0
        print (self.name, ' sleep ', time, ' hour(s)')

    def Work(self):
        print ('Person Work')

class Student(Person):
    def __init__(self, name, sex, age, ID, school, stuId):
        super(Student, self).__init__(name, sex, age, ID)
        self.school = school
        self.stuId = stuId

    def Work(self):
        print ('Student Work: Learn')

class Worker(Person):
    Count = 0
    def __init__(self,name, sex, age, ID, company, teachnical, workExperience):
        super(Worker, self).__init__(name, sex, age, ID)
        self.company = company
        self.teachnical = teachnical
        self.workExperience = workExperience
        Worker.Count += 1

    def Work(self):
        print ('Worker work: code')

    def __del__(self):
        Worker.Count -= 1
        del(self)

### Test code ###

worker = Worker(1,2,3,4,5,6,7)
worker2 = Worker(2,3,4,5,6,7,8)

print (Worker.Count) # 2
del (worker2)
print (Worker.Count) # 1
worker.Work() # Worker work: code
print (worker.name, worker.age,worker.teachnical) # 1 3 6

stu = Student(1,2,3,4,5,6)
stu.Work() # Student Work: Learn
stu.eat("apple") # 1 eat apple
print (stu.name, stu.age, stu.school) # 1 3 5

per = Person(1,2,3,4)
per.Work() # Person Work
per.sleep(3.0) # 1 sleep  3.0  hour(s)
per.sleep(-10) # 1 sleep  6.0  hour(s)