# 用户登陆（三次输错机会），且每次输入错误时显示剩余错误次数（提示：使用字符串格式化）
i = 3
username = "yangxiaoer"
password = "123456"
while i>0:
    i=i-1
    name = input ("请输入你的用户名: ")

    if name == username:
        passwd = input("请输入你的密码: ")
        if passwd == password:
            print("登陆成功")
            print("""
             username:%S
             password:%s
            """%(username,password))
        else:
            if i==0:
                print("您的机会已经用光，结束本次操作。")
                break
            print("你的密码错误，请重新输入")
            print("你还有%s次的机会"%(i))
            continue
    else:
        print("你的用户名错误，请重新输入：")
        print("你还剩是%s次机会"%(i))
