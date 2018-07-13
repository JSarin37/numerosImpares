# Julio Cajamarca
# Codigo para imprimir los numeros impares en el rango de 100 a 1 y sumarlos
n = 100
h = 0
while n >= 1:
    if n%2 != 0:
        print (n),
        h += n
    n -= 1
print ('La suma de los numeros es: %i' % h)
