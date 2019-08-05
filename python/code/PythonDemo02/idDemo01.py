a = 20
b = 20

if a is b:
    print("a和b是相同的标识")
else:
    print("a和b不是同一个标识")

if id(a) == id(b):
    print("a=b")
else:
    print("a!=b")


b = 30
if a is b:
    print("a=b")
else:
    print("a!=b")