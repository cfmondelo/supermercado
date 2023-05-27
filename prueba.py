import hashlib
print("Hola, esto es una prueba")
contraseña="vistaalegre"
def cifrarContra(contra):
   # Creamos el objeto de clase hash y le pasamos la contraseña en byte string a cifrar
  h = hashlib.new("sha256", contra.encode())
  # Convertimos la contraseña cifrada en hexadecimal
  contraCif = str(h.hexdigest()) 
  return contraCif
print(cifrarContra(contraseña))