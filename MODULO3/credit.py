
def validacion():
    while True:
        try:
            global tarjeta
            tarjeta = int(input("INTRODUCE UN NUMERO DE TARJETA DE CREDITO: "))
            global m
            m = 0
            str(tarjeta)
            global lista_tarjeta
            lista_tarjeta = []
            
            for i in str(tarjeta):
                lista_tarjeta.append(i)
                m += 1
            
            while(m<13 or m>16 or m==14):
                print("Error, tarjeta invalida, debe tener 13, 15 o 16 digitos")
                tarjeta = int(input("INTRODUCE UN NUMERO DE TARJETA DE CREDITO: "))
                m=0
                i=0
                for i in str(tarjeta):
                    lista_tarjeta.append(i)
                    m += 1
            break

        except:
            print("Ocurrio un error, introducir bien el numero")


def validacion_2():
    
    if m == 13:
        print("***TARJETA VISA***")
        if lista_tarjeta[0] == '4':
            pass
        else:
            print("Incorrecto, la tarjeta visa empieza con '4' ")
            return 1
           
                  
    elif m==15:
        print("***TARJETA AMEX***")
        if lista_tarjeta[0] == '3' and (lista_tarjeta[1] == '4' or lista_tarjeta[1] =='7'):
            pass
        else:
            print("Incorrecto, la tarjeta amex empieza con '34' o '37' ")
            return 1
      
    else: 
        
        if lista_tarjeta[0] == '4':
            print("***TARJETA VISA***")
        
        elif (lista_tarjeta[0] == '5' and (lista_tarjeta[1]=='1' or lista_tarjeta[1]=='2' or lista_tarjeta[1]=='3' or lista_tarjeta[1]=='4' or lista_tarjeta[1]=='5')):
            print("***TARJETA MASTERCARD***")
        
        else:
            print("Incorrecto")
            return 1
      
validacion()

validacion_2()

while validacion_2() == 1 :
    validacion()
    validacion_2()



#ALGORITMO DE LUHN
suma = 0
sum_total = 0
sum_cifra = 0
if m == 13 or m ==15:
    for j in range(1,m,2):
        num = int(lista_tarjeta[j]) * 2
        while num > 0:
            D = num % 10
            sum_cifra += D
            num = num // 10
        sum_total += sum_cifra
        sum_cifra = 0
    print(sum_total)

    for k in range(0,m,2):
        suma += int(lista_tarjeta[k])

    sum_total += suma
    print(sum_total)
    if sum_total % 10 == 0:
        print("Es una tarjeta valida")
    else:
        print("Es una tarjeta invalida")
        
else:
    for l in range(0,m,2):
        num = int(lista_tarjeta[l]) * 2
        while num > 0:
            D = num% 10
            sum_cifra += D
            num = num // 10
        sum_total += sum_cifra
        sum_cifra = 0


    for k in range(1,m,2):
        suma += int(lista_tarjeta[k])

    sum_total += suma

    if sum_total % 10 == 0:
        print("Es una tarjeta valida")
    else:
        print("Es una tarjeta invalida")
    
        

        

