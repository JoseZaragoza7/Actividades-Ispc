"""2)   Crear una lista en Python denominada “Dueno2”  y recorrerla con un bucle  mostrando sus elementos por pantalla con excepción del DNI y el apellido. 
Los elementos de la lista son:

           23546987,  “Maria”,  “Perez”, 4789689,  “Pueyrredon  811”

 que representan los datos del dueño de un perro (DNI, nombre, apellido, teléfono y dirección) """


DNI=23546987
nombre= "Maria"
apellido="Perez"
telefono=4789689
direccion="Pueyrredon 811"
 
Dueno2=[DNI, nombre, apellido, telefono, direccion]

lista_Dueno2 = [x for x in Dueno2 if x!=telefono and x!=DNI]
print(lista_Dueno2)

