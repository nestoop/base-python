if __name__ == "__main__":
    lanages = ['java', 'c++', "javaScript", "scala", "python", "go", "typeScript"]
    for lanage in lanages:
        print(lanage, len(lanage))
    for i in range(len(lanages)):
        print(i, lanages[i])
    for i in range(0, len(lanages)-1):
        print(i, lanages[i])
    print(list(lanages))

    for i in range(2, 3):
        print(i)

    for i in range(2, 10):
        for k in range(2, i):
            if i % k == 0:
                print("i:", i, "k:", k, "*", i//k)
                break
            else:
                print(i, "is prime number")
