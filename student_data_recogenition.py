system={}
print("""
1.添加学生信息
2.修改学生信息
3.删除学生信息
4.查询学生信息
5.列出学生信息
6.统计全部学生
7.退出
""")
while True:
    choice=int(input("你的要求是"))
    match choice:
        case 1:
            name=input('你的名字是')
            math=input('数学分数是')
            chinese=input('chinese分数是')
            English=input('english分数是')
            system[name]={"math":math,'chinese':chinese,'English':English}
            continue
        case 2:

            name=input("what's your name?")
            if name in system:
                math = input('数学分数是')
                chinese = input('chinese分数是')
                English = input('english分数是')
                system[name] = {'math': math, 'chinese': chinese, 'English': English}
                continue
            else:
               print("you are wrong")
        case 3:
            name = input("what's your name?")
            if name in system:
                del system[name]
            else:
                print('not exist')
            continue

        case 4:
            name=input("what's your name?")
            if name in system:
                print(system[name])
            else:
                print("you are wrong")
        case 5:
            for i in system:
                print(system[i])

        case 6:
            if not system:
                print("you are wrong")
            else:

                best_enlish_score=max(int(i ['English']) for i in system.values())
                print(best_enlish_score)
                best_chinese_score=max (int(i ['chinese']) for i in system.values())
                print(best_chinese_score)
                best_math_score = max(int(i['math']) for i in system.values())
                print(best_math_score)



        case 7:
            break


