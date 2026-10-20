def add(a,b):
    return a+b
def sub(a,b,sum):
    return sum(a,b)
def mul(*args,**kwargs):
    return sum(*args,**kwargs)
print(add(1,2))
print(sub(2,3,DEE))
print(mul(1,2,3,round=2,print=True))