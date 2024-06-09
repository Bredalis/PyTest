
# Librerias para modificar la ruta

import sys
import os

# Insertar el directorio principal del archivo actual
sys.path.insert(0, os.path.abspath(os.path.join(
	os.path.dirname(__file__), "..")))

# Libreria para testing

import pytest
from main import suma, mayor_que, login

def test_suma():
	assert suma(2, 5) == 7

def test_mayor_que():
	assert mayor_que(6, 5)

@pytest.mark.parametrize(
	"input_x, input_y, expected",
	[
		(5, 1, 6), 
		(6, suma(4, 2), 12),
		(suma(19, 1), 15, 35),
		(-7, 10, suma(-7, 10))
	]
)

def test_suma_parametros(input_x, input_y, expected):
	assert suma(input_x, input_y) == expected

def test_login_pasado():
	assert login("Bredalis", "12345")

def test_login_fallado():
	assert not login("Angelica", "1234567")