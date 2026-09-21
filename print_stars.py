fruits=['apple','banana','orange']
fruits.append('grape')
del fruits[1]
fruits[2 ]='strawberry'
print(fruits)
print(len(fruits))

def collect_scores():
    scores=[]
    for i in range(3):
        s=int(input("输入你的成绩"))
        scores.append(s)
    print(scores)
    print(len(scores))
    return scores
print(type(collect_scores()))
collect_scores()




