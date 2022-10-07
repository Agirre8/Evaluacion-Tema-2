def dividir (numerador, divisor):
    return numerador/divisor

try:
    resultado = dividir(7, 0)
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir entre 0")


lista = [4,7,30,23,5]

index=10

if 0 <= index < len(lista):
    lista[index]
else:
    print("Elemento fuera de la lista")



