import string
def probando():
    try:
        global k
        k = int(input("Introduzca un número entero no negativo: "))
        while k <= 0:
            print("Error, ingrese un numero entero no negativo: ")
            k = int(input(""))
        

    except:
            print("ERROR, el programa solo acepta unicamente números")
            probando()

probando()
#Guardar el abecedario en una variable: abcdefghijklmnopqrstuvwxyz
ALFABETO = string.ascii_lowercase




#Pedir una frase a cifrar
plaintext = input("Ingrese una frase: ")

#Texto cifrado
ciphertext = ''

#Cifrando
for i in plaintext:

    if i.lower() in ALFABETO:
        
        #Para encontrar la posicion de la letra
        p = ALFABETO.find(i.lower())

        #Nueva posicion de la letra (aumentando de posicion)
        c = (p+k) % 26

        if i.isupper():
            ciphertext += ciphertext.join(ALFABETO[c].upper())
        else:
            ciphertext += ciphertext.join(ALFABETO[c])
    else:
        ciphertext += ciphertext.join(i)
print(ciphertext)

