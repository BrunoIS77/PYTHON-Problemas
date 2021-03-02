
def acept_num():
    try:
        global altura
        altura = int(input('Digite el tamaño de la altura(entre 1 y 8): '))
        
        while (altura<=0 or altura>8):
            print("ERROR, vuelva a digitar la altura:")
            altura = int(input(''))
    except:
        print("ERROR, No puede ingresar letras, solo numeros enteros\n Ingrese correctamente")
        acept_num()
acept_num()


    
for i in range(altura):
    print(' '*(altura-i+1) + "#"*(i+1))




