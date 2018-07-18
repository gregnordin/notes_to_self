import pkg as pg
print(dir())
print(dir(pg))

a1 = pg.A1()
a2 = pg.A2()
b1 = pg.B1()
b2 = pg.B2()

print('-------------')

from pkg import A1, A2, B1, B2
print(dir())

aa1 = A1()
aa2 = A2()
bb1 = B1()
bb2 = B2()

# Output
'''
    $ python tryit.py
    ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'pg']
    ['A1', 'A2', 'B1', 'B2', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'a', 'b']
    Class A1
    Class A2
    Class B1
    Class B2
    -------------
    ['A1', 'A2', 'B1', 'B2', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a1', 'a2', 'b1', 'b2', 'pg']
    Class A1
    Class A2
    Class B1
    Class B2
'''