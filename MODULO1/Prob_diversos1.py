deposito = float(input('Ingrese la cantidad depositada: '))

primer_año = 1.04 * deposito
segundo_año = 1.04 * primer_año
tercer_año = 1.04 * segundo_año

print('La cantidad ahorrada el primer año es:',round(primer_año,2))
print('La cantidad ahorrada el segundo año es:',round(segundo_año,2))
print('La cantidad ahorrada el tercer año es:',round(tercer_año,2))

