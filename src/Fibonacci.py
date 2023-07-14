# f(0)=0 ; f(1)=1 ; f(n)=f(n-1)-f(n-2)


# method 1 (slow)
def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


import sys


if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

num = int(sys.argv[1])
print(fib(num))

# method 2 (fast)
l = [0, 1]
num = int(sys.argv[1])
if num == 0:
    l = [0]
elif num == 1:
    l = [0, 1]
else:
    num -= 1
    for i in range(num):
        l.append(l[-2] + l[-1])
print(l)
