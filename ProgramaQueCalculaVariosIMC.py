# Programa que toma varias personas y calcula su IMC
def CalcularIMC(lectura):
  dic = {}
  for i in lista:
    columna = i[0] #Se itera sobre los nombres de las personas
    p = i[1]#Se itera sobre el peso de las personas
    a = i[2]#Se itera sobre la altura de las personas
    c = p/(a**2) #Se hace el calculo del IMC

    #Se evalua la condicion del IMC
    if c < 18.5:
      j="IMC Bajo"
      dic[columna] = j #Se agrega el mensaje a cada nombre iterado al principio
    elif 18.5 <= c and c < 25:
      j="IMC Normal"
      dic[columna] = j #Se agrega el mensaje a cada nombre iterado al principio
    elif 25 <= c and c <= 30:
      j="IMC Sobrepeso"
      dic[columna] = j #Se agrega el mensaje a cada nombre iterado al principio
    else:
      j="IMC Obesidad"
      dic[columna] = j #Se agrega el mensaje a cada nombre iterado al principio
  print(dic) #imprimimos el diccionario con sus nuevos valores
  return
#Creamos la lista con los datos de las personas
lista=[("Matias",30,1.89), ("Jose", 80, 1.70), ("Miguel", 110, 1.65), ("Franco", 65, 1.80), ("Julian", 65, 1.97)]
CalcularIMC(lista) #Llamado a la funcion creada anteriormente