def func():
    x = 1
    while x < 100:
        y = (yield x)
        x += y
        print(y)


geniter = func()
geniter.__next__()
print(11)
geniter.send(3)
