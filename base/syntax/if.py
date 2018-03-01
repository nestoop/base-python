if __name__ == "__main__":
    if True:
        print("if condition.....")
    x = int(input("键盘输入的数据:"))
    if x < 10:
        print("x的值小于10，x值为 ", x)
    elif x > 11 & x < 80:
        print("x的值大于11,小于60，值为", x)
    elif x > 100:
        print("哎呀，妈呀，x终于大于100")
    elif x == 80:
        print("x的值等于80")
    else:
        print("if 的 else 分支")
