money=1000
for i in range(1,21):
    import random
    num = random.randint(1,10)
    if num <=5:
        print(f'员工{i},绩效{num},不给')
        continue
    if money>=100:
        money-=100
        print(f"给你了,还有{money}")
    else:
        break





 0