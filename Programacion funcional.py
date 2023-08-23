"""
def factorial(n):
    return 1 if n == 0 else n*factorial(n-1)

numero=int(input("ingrese numero que desea saber factorial: "))

resultado=factorial(numero)
print("El factorial de",numero)
print("Es:",resultado)
"""

lista=[1,2,3,4,5,10]
def pordos(x):
    return x*2
lista_pordos=map(pordos,lista)
print(list(lista_pordos))


"""
lista=[1,2,3,4,5]

lista_pordos=map(lambda x:2*x,lista)
print(list(lista_pordos))
"""

"""
lista=[5,8,12,1,9,15,20]

def espar(x):
    return x % 2 == 0

pares=filter(espar,lista)

print(list(pares))
"""

"""
lista=[5,8,12,1,9,15,20]
pares=filter(lambda x:x%2==0,lista)

print(list(pares))
"""