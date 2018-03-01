def function_operate_queue():
    from collections import deque
    queue = deque(['aa', 'bb', 'cc'])
    print(queue.popleft())
    print(queue)
    print(queue.popleft())
    print(queue)


def function_queue_lambda():
    queue = list(map(lambda x: x ** 2, range(10)))
    print(queue)

    queue1 = []
    for x in range(10):
        queue1.append(x**2)
    print(queue1)

    queue2 = [x**2 for x in range(10)]
    print(queue2)


if __name__ == "__main__":
    lists = ['a', 'b', 'a', 'c', 'd', 'b', 'e', 'f']
    print(lists.count('a'))
    print(lists.index('f'))
    print(lists.index('b', 3))
    lists.reverse()
    print(lists)
    lists.append('g')
    print(lists)
    print(lists.pop())
    print(lists)
    print("--------queue operation----------")
    function_operate_queue()
    function_queue_lambda()
