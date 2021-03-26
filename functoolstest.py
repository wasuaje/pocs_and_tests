# -*- coding: utf-8 -*-
from functools import partial

def power(base, exponent):
    return base ** exponent



square = partial(power, exponent=2)
cube = partial(power, exponent=3)

#esto se ejecuta con unittes, lo llamas con unitest y debe coincidir|
def test_partials():
    assert square(2) == 4
    assert cube(2) == 8


print square(2)
print cube(2)
