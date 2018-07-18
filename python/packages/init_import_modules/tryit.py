import pkg as pg
print(dir())
print(dir(pg))

a1 = pg.a.A1()
a2 = pg.a.A2()
b1 = pg.b.B1()
b2 = pg.b.B2()

# Output
'''
    $ python tryit.py
    ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'pg']
    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'a', 'b', 'pkg']
    Class A1
    Class A2
    Class B1
    Class B2
'''