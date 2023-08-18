#Se define la lista y se le pide al usuario la cantidad de alumnos a ingresar.
c=0
lista=[]
cantidad=int(input("¿Cuantos alumnos desea ingresar?: "))

while cantidad > c: #Se evalua la condicion de la cantidad de alumnos a ingresar
    c = c + 1
    aprobados=[] #lista de las personas aprobadas y desaprobadas
    desaprobados=[]
    nombre=input("Ingrese el nombre del alumno: ")
    nota=float(input("Ingrese la nota del alumno: "))
    lista.append((nombre, nota)) #Se agrega cada alumno con su nombre y su nota a la lista

for i in lista:
        a=i[0] #Se recorre sobre los nombres
        n=i[1] #Se recorre sobre las notas
        if n >= 6: #Se evalua si las notas son mayores o iguales a 6
            aprobados.append(a) #Se guarda en la lista el nombre de las personas que aprueban
        else:
            desaprobados.append(a) #Se guarda en la lista el nombre de las personas que desaprueban

print("Los alumnos que aprobaron son:", aprobados) #Se imprime por pantalla dicha lista
print("Los alumnos que desaprobaron son:", desaprobados)
