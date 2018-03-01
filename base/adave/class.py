def outSide():
    print("outside method")

class MyClass:

    sharedVar = "testVariable"

    f = outSide

    def __init__(self, args1: object, args2: object) -> object:
        self.ar1 = args1
        self.ar2 = args2

    def test(self):
        return "test class method"

if __name__ == "__main__":

    xx = MyClass("jjj", "babb")
    print(xx.ar1)
    print(xx.ar2)
    print(xx.sharedVar)

    test1 = xx.test
    print(test1())

    xxx = MyClass("jjj", "test")

    print(MyClass.f)

