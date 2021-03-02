def alumnos():
    try:
        global n
        n = int(input("Ingrese la cantidad de alumnos: "))
        while (n <= 0):
            print("Error, Ingrese un cantidad entera no negativa: ")
            n = int(input(""))
    except:
        print("ERROR, Ingrese solo numeros:")
        alumnos()

alumnos()

lista_alumnos = []
notas_alumnos = []
datos = {}

for i in range(n):
    nombre = input("\nIngrese el nombre del alumno {}: ".format(i+1))
    datos['nombre'] = nombre
    
    for j in range(3):

        notas = int(input("Ingrese la nota {} del alumno: ".format(j+1)))

        while (notas<0 or notas>10):
            print("Error, las notas deben estar en el rango de 0 a 10: ")
            notas = int(input("Vuelva a ingresar la nota {} del alumno {}: ".format(j+1,nombre)))
        datos['nota{}'.format(j+1)] = notas

    lista_alumnos.append(datos)
    print(lista_alumnos)




