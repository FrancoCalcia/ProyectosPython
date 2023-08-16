#Funcion que devuelve el IMC de una persona en base a su altura y su peso.
def IMC(p,h): #Se define la funcion
  C=p/(h**2) #Se hace el calculo para el indice de masa corporal
  print("El indice de la masa corporal es de:",C) #Se retorna dicho calculo
  return

p=float(input("Ingrese el peso de la persona expresada en Kilogramos: ")) #Se pide el peso de la persona en Kilogramos.
h=float(input("Ingrese la altura de la persona expresada en metros: ")) #Se pide la altura de la persona expresada en metros.
IMC(p,h) #Se llama a la funcion