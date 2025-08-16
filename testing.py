##Generador de contraseñas automatico##
import string
import random

print("Estes es un generador de contraseñas automático")

def generar_contraseña(longitud=12):
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    
    return contraseña

print("Contraseña generada:", generar_contraseña())