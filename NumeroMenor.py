#Funcion que devuelve el menor numero de la lista que se le envie para evaluar
def minimo(lista):
  lista.sort() #Se ordena la lista de menor a mayor
  print(lista[0])#Se busca el primer numero de la lista ordenada y se retorna ese valor. En este caso es el -9
  return 


lista=[3,8,1,2,-9,6,0,-3,-6] #se define la lista

minimo(lista) #Se llama a la funcion con la lista creada
