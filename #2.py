a = int(input("a: "))
b = int(input("b: "))
s = 0
if a < b:
    while a < b+1:
        if a % 2 == 0:
            print(a)
            s += a
        a += 1
    print(s)
else:
    while a > b:
        if a % 2 == 0:
            print(a)
            s += a
        a -= 1
    print(s)
