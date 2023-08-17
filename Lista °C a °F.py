#Funcion que convierte una lista a de grados Celcius a Fahrenheit
def Conversion(c):
    Far=[]
    for i in c:
        F = i * (9/5) + 32
        Far.append(F)
    print(Far)
    return

GradosCelsius=[43, 21, 12, 5, 36]
Conversion(GradosCelsius)