nums=[1,5,2,5,1,3]

print(sorted(set(nums)))
f=1
dict_1={}
text ="hello"
for i in text:

    if i in dict_1:
        dict_1[i] += 1
    else:
        dict_1[i] = f
print(dict_1)
students = [
    {"name": "张三", "score": 88},
    {"name": "", "score": 95},
    {"name": "王五", "score": 90}
]
best_score=max(int(i["score"]) for i in students)
print(f"李四,fenshu:{best_score}")


cart = {
    "苹果": [2, 5.0],   # 第一个数字是数量，第二个数字是单价
    "香蕉": [3, 2.5],
    "牛奶": [1, 12.0]
}

total = 0
for i in cart.values():
    total+=i[0]*i[1]
print(total)
