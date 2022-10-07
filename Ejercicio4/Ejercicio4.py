def dividir (numerador, divisor):
    return numerador/divisor

try:
    resultado = dividir(7, 0)
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir entre 0")


lista = [4,7,30,23,5]

elemento=10

if 0 <= elemento < len(lista):
    lista[elemento]
else:
    print("Elemento fuera de la lista")


paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
try:
    paises["alemania"]
except KeyError:
    print("pais no registrado")

resultado = "2" +10


