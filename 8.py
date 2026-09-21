import random
num=random.randint(1,10)
n=int(input("guess the number"))
if n==num:
    print("yes")
else:

    n = int(input("guess the number"))

    if n==num:

        print("yes")
    else:

        n = int(input("guess the number"))

        if n==num:
            print("yes")
        else:
            print("lose")



