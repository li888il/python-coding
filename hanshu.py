#传参方式
def reg_stu(name,age,gender,city):
    print(name,age,gender,city)
    return {"name":name,"age":age,"gender":gender,"city":city}
stu=reg_stu("zhangxa",12,"dfsa","fasdf")
print(stu)
sss=reg_stu(name="zhangxa",city="dfs",gender="fadf",age=12)
print(sss)
stud=reg_stu("zhangxa",12,"ff",city="dfa")#混合传参




#默认参数
def reg_stu(name,age,gender,city="dfs"):#默认值
    print(name,age,gender,city)
    return {"name":name,"age":age,"gender":gender,"city":city}
sti=reg_stu(12,"dfs","dfa")
