import string


#Guardar el abecedario en una variable: abcdefghijklmnopqrstuvwxyz
ALFABETO = string.ascii_lowercase


otro = "ytnshkvefxrbauqzclwdmipgjo"

#Pedir una frase a cifrar
plaintext = input("Ingrese una frase: ")

#Invocando cadena para Texto cifrado
ciphertext = ''

#Cifrando
for i in plaintext:

    if i.lower() in ALFABETO:
        
        #Para encontrar la posicion de la letra
        p = ALFABETO.find(i.lower())
        
        if i.isupper():
            ciphertext += ciphertext.join(otro[p].upper())
        else:
            ciphertext += ciphertext.join(otro[p])
    else:
        ciphertext += ciphertext.join(i)
        
print(ciphertext)

