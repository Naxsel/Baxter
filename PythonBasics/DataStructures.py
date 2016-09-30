# Lists
a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25), a.count('x')
a.insert(2, -1)
a.append(333)
print a
a.remove(333)
print a
a.reverse()
print a
a.sort()
print a
a.pop()

# Functional Programming Tools

def f(x): return x % 3 == 0 or x % 5 == 0

print filter(f, range(2, 25))

def cube(x): return x*x*x

print map(cube,range(1,11))
print filter(cube,range(1,11))