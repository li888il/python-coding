username=input("用户名")
password=input("情输入密码")
def login(password):
    for i in (1,3):

        if password == "123456" and username == "admin":
            print(f"登录成功，欢迎{username}")
            return
    for i in range(1,4):
            print(f"用户名或密码错误，还有{3-i}次机会")
            break
    username = input("用户名")
    password = input("情输入密码")
    print("失效")


login(password)
