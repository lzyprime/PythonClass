// 作业:
// 定义一个人类（Person）
// 属性包括:姓名，性别，年龄，ID，
// 行为：吃，睡，工作
// 定义一个学生子类继承人类（Student）
// 增加属性：学校，学号
// 行为：重写工作方法（学习）
// 定义一个员工子类继承人类（Worker）
// 增加属性：公司名称，技术方向，工作年限
// 行为：重写工作方法（写代码）
// 实例化员工对象，要统计该类一共已经有了多少员工对象
// 编写测试函数，对上述实现进行测试

#include <bits/stdc++.h>
using namespace std;

class Person
{
  public:
    Person(const string n, const string s, const string I, const int a)
        : name(n), sex(s), ID(I) {}

    Person(const Person &) = default;

    Person &operator=(const Person &) = delete;

    Person &eat(const string food)
    {
        cout << name << " eat " << food << endl;
        return *this;
    }

    const Person &eat(const string food) const
    {
        cout << name << " eat " << food << endl;
        return *this;
    }

    Person &sleep(double t = 6)
    {
        cout << name << " sleep " << (t > 0 ? t : 6) << "hour(s)" << endl;
        return *this;
    }

    const Person &sleep(double t = 6) const
    {
        cout << name << " sleep " << (t > 0 ? t : 6) << "hour(s)" << endl;
        return *this;
    }

    virtual Person &work()
    {
        return *this;
    }

    virtual const Person &work() const
    {
        return *this;
    }

    virtual ~Person() = default;

  protected:
    string name, sex, ID;
    int age;
};

class Student : public Person
{
  public:
    Student(const string n, const string s, const string I,
            const int a, const string sch, const string s_i)
        : Person(n, s, I, a), school(sch), stu_id(s_i) {}

    Student(const Person &a, const string sch, const string s_i)
        : Person(a), school(sch), stu_id(s_i) {}

    Student &work() override
    {
        cout << name << " student work: learn" << endl;
        return *this;
    }

    const Student &work() const override
    {
        cout << name << " student work: learn" << endl;
        return *this;
    }

  private:
    string school, stu_id;
};

class Worker : public Person
{

  public:
    Worker(const string n, const string s, const string I,
           const int a, const string c, const string t, const string w)
        : Person(n, s, I, a), company(c), teachnical(t), work_exp(w)
    {
        count++;
    }
    Worker(const Person &a, const string c, const string t, const string w)
        : Person(a), company(c), teachnical(t), work_exp(w)
    {
        count++;
    }

    Worker(const Worker &) = delete;
    Worker &operator=(const Worker &) = delete;

    Worker &work() override
    {
        cout << name << " Worker work : code" << endl;
        return *this;
    }

    const Worker &work() const override
    {
        cout << name << " Worker work : code" << endl;
        return *this;
    }

    static const int getCount()
    {
        return count;
    }
    virtual ~Worker() override
    {
        count > 0 ? count-- : 0;
    }

  private:
    string company, teachnical, work_exp;
    static int count;
};

int Worker::count = 0;

// test code //
int main()
{
    Person per1("lzy", "man", "3821", 20);
    (per1.eat("fff")).work();

    Student stu_per1(per1, "DNUI", "617");
    ((stu_per1.eat("22")).work()).work();

    Worker wk_per1(per1, "no", "bzd", "20");
    ((wk_per1.work()).work()).sleep(8);

    Person *wk2 = new Worker(per1, "2", "2", "2");

    wk2->work();
    cout << Worker::getCount() << endl;
    delete wk2;
    wk2 = 0;
    cout << Worker::getCount() << endl;
    return 0;
}

/* 
lzy eat fff
lzy eat 22
lzy student work: learn
lzy student work: learn
lzy Worker work : code
lzy Worker work : code
lzy sleep 8hour(s)
lzy Worker work : code
2
1
*/