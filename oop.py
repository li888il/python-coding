class Student:  # 定义类，类名首字母大写
    def __init__(self, name, score):  # 创建对象时自动调用
        self.name = name    # self 指这个对象自己，把 name 存到对象上
        self.score = score  # 把 score 存到对象上

    def show(self):  # 实例方法，用 对象.show() 调用
        print(f"{self.name}: {self.score}")  # 通过 self 访问对象自己的数据

s1 = Student("张三", 88)  # 创建对象，自动调用 __init__
s2 = Student("李四", 92)
s1.show()  # 输出：张三: 88
s2.show()  # 输出：李四: 92
print(s1.name)
#class Student:          ← 设计一张空白表（模板）
#    __init__ ...        ← 规定：填表时把名字、年龄写到"我自己这张表"上
#    introduce ...       ← 规定：读出"我自己这张表"的内容拼成句子
#
#
#s = Student("小明", 18)
#   │
#   ├─ 抽一张新表
#   ├─ 执行 __init__：self=这张新表
#   │     这张表.name = "小明"
#   │     这张表.age  = 18
#   └─ 把这张表命名为 s
#
#
#s.introduce()
#   │
#   └─ 执行 introduce：self=s（小明这张表）
#         读 s.name="小明"，s.age=18
#         返回 "我是小明，今年18岁"
input()
