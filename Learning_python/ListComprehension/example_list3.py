#Crea una lista con los cuadrados de los números del 1 al 100.
result=[x*x for x in range(1,101)]
print (result) 
print(" ")
#Crea una lista con los números pares del 1 al 20.
result2=[x for x in range(1,20) if x%2==0]
print(result2)
#Crea una lista con los números impares del 1 al 120.
result3=[x for x in range(1,120) if x%2!=0]
print(result3)
#A partir de 2 listas de números enteros (a y b) Ejemplo:
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
#crea una lista con los elementos que están en ambas listas a y b.
a.extend(b)
print(a)
#Utilizando las 2 listas del ejercicio anterior, crea una lista con los elementos 
#que están en la lista a pero no en la lista b.
c = []
for x in a:
    if x == a:
        c.append(x)
print(c)





