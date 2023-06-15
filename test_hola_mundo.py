from hm import hola_mundo
import pytest

def test_hm():
    assert hola_mundo()=="Hola Mundo!"

test_hm()

x = 4
y = x
z = y
c = y
ct = y
y = y