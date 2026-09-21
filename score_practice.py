scores=[]
for i in range(5):
    s=int(input(f"请输入第{i+1}个学生成绩"))
    scores.append(s)
print(scores)
print(max(scores))
print(min(scores))