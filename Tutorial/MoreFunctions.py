def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print f(1)
print f(3)
print f(5)