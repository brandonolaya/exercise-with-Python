def increment (*arg):
    return sum(arg)

num = lambda *arg: sum(arg*2)

print(f'lambda * 2 es {num(4,5,6,7)}')
print(increment(4,5,6,7))