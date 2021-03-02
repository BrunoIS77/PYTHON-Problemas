import math
print('\n***ECUACION DE 2DO GRADO***')
print("ax² + bx + c = 0")
print('a ≠ 0')

a = int(input('Digite el valor de a: '))


while a==0:
    print('ERROR, "a" no puede ser igual a 0')
    a = int(input('Digite el valor de a: '))

b = int(input('Digite el valor de b: '))
c = int(input('Digite el valor de c: '))

discriminante = pow(b,2) - 4*a*c

if discriminante >=0:
    if discriminante>0:
        x1 = -b + pow(discriminante,1/2)
        x2 = -b - pow(discriminante,1/2)
        print("La primera solucion es:",x1)
        print("La segunda solucion es:",x2)
    else:
        x = -b/(2*a)
        print("La solucion unica es:",x)
else:
    print("Ecuacion no presenta solucion real")