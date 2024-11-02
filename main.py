
# Funciones para realizar testing

def suma(x, y):
	"""Retorna la suma de x e y."""
	return x + y

def mayor_que(num_1, num_2):
	"""Retorna True si num_1 es mayor que num_2, de lo contrario False."""
	return num_1 > num_2

def login(nombre_usuario, contrasena):
	"""
	Verifica si el usuario y la contraseña son correctos.

	Args:
		nombre_usuario (str): Nombre del usuario a verificar.
		contrasena (str): Contraseña del usuario a verificar.

	Returns:
		bool: True si los argumentos son correctos y False si no lo son.
	"""

	return nombre_usuario == "Bredalis" and contrasena == "12345"