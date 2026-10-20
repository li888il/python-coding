
numlist1=[1,2,233,4,5,6]
numlist2=[1,233,434,344,3453,36,233]
numlist1.extend(numlist2)#newlist=newlist1+newlist or newlist=[*newlist1,*newlist2}
print(numlist1)
newlist=[]
for num in numlist1:
    if num in newlist:#可删去else，改为not in.
        continue
    else:
        newlist.append(num)
print(newlist)


