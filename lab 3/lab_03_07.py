# аргументы функции
def sum(x, y, z=1):
    return x + y + z


print("sum(1,2,3): ", sum(1, 2, 3))
print("sum(1,2): ", sum(1, 2))
print("sum(x=1,y=3): ", sum(x=1, y=3))


# переменное количество аргументов
def printArgs(*args):
    print("args of printArgs(): ", args)
    return


# переменное количество аргументов и аргументов-ключевых слов
def printArgsnKwargs(m, *args, **kwargs):
    print("main argument of printArgsnKwargs(): ", m)
    print("args of printArgsnKwargs(): ", args)
    print("args of printArgsnKwargs(): ", kwargs)
    return


printArgs("Hello World!", 1, 3, 5)
printArgsnKwargs("Earth", 7.125, radius=6371, pos=3)
print("\n")


# 19
def checkArgs(*args, **kwargs):
    if len(args) <= 3 & len(kwargs) < 3:
        print(args, kwargs)
    else:
        print("Превышено количество аргументов!")
    return
