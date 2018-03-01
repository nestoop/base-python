class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


class DemoException(Exception):
    def __init__(self, x: object, y: object):
        self.xx = x
        self.yy = y


if __name__ == "__main__":
    for cls in [B, C, D]:
        try:
            print("111111")
            raise cls()
            print("232323")
        except D:
            print("exception D")
        except C:
            print("exception C")
        except B:
            print("exception B")
        try:
            i = int(input("please input number:"))
            print("input i:", i)
        except Exception:
            print("oops input data is not number, try again")
        finally:
            print("finally")

        try:
            x = 4
            y = 3
            if x % y > 0:
                print("x:", x, "y:", y)
                raise DemoException(x, y)
            print("23232323233")
        except DemoException as demo:
            print(demo.xx / demo.yy)
            break
