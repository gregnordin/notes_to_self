import pkg.a, pkg.b
from pkg.a import A1
from pkg.b import B1
print(dir())
print(dir(pkg))

a1 = A1()
a2 = pkg.a.A2()
b1 = B1()
b2 = pkg.b.B2()

# Output
'''
    $ python tryit.py
    ['A1', 'B1', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'pkg']
    ['__doc__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'a', 'b']
    Class A1
    Class A2
    Class B1
    Class B2
'''
