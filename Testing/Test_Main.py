
# Librerías para modificar la ruta
import sys
from pathlib import Path

# Insertar el directorio principal del archivo a testear
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Librería para testing
import pytest
from main import suma, mayor_que, login

def test_suma():
	"""Prueba la función suma."""
	assert suma(2, 5) == 7

def test_mayor_que():
	"""Prueba la función mayor_que."""
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
	"""Prueba la función suma con parámetros variados."""
	assert suma(input_x, input_y) == expected

def test_login_exitoso():
	"""Prueba el inicio de sesión exitoso."""
	nombre_usuario = "Bredalis" 
	contrasena ="12345"

	assert login(nombre_usuario, contrasena)

def test_login_fallido():
	"""Prueba el inicio de sesión fallido."""
	nombre_usuario = "Angelica" 
	contrasena ="1234567"

	assert not login(nombre_usuario, contrasena)