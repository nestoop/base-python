def function1(n):
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a + b
        print()


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes', 'Y', 'YE', 'YES'):
            return True
        if ok in ('n', 'no', 'NO'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError("参数错误")
        print(reminder)


def function_test(a, L=[]):
    L.append(a)
    return L


def function_test1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


def function_test2(args1, *args2, **args3):
    print("single data element", args1)
    for arg in args2:
        print("args2 element", arg)

    keys = sorted(args3.keys())
    for key in keys:
        print("directory element,key :", key, " value: ", args3[key])


if __name__ == "__main__":
    function1(10)
    # ask_ok('Do you really want to quit!')
    # ask_ok('OK to overwrite the file!', 2)
    # ask_ok('OK to overwrite the file!', 2, 'Come on ,only yes or no')
    print(function_test(1))
    print(function_test(2))
    print(function_test(3))

    function_test2("aaa", "bbbb", "cccc", "dddd", ee="eeee", ff="fffff", gg="gggg")
