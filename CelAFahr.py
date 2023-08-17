#Funcion que recibne temperaturas en grados Celsius
#y devuelve temperaturas en grados Fahrenheit

def conversion(C):
    F = C * (9/5) + 32
    print(F)
    return
Celsius=float(input("Ingrese los grados a convertir: "))
conversion(Celsius)