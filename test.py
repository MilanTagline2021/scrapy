def test():
    for a in range(10):
        yield a

k = test()
print(k)
