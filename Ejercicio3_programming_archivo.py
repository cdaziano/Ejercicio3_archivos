import os
os.system('cls')

alumnos = []
archivo = open("alumnos.txt", "r")
alumnos = archivo.readlines()
archivo.close()


def agregar(alumnos):
    archivo = open("alumnos.txt", "a+")
    nom = input("Ingrese Nombre y Apellido: ")
    nom = nom.title()
    archivo.write(nom + "\n")
    archivo.close()
    print("Dato Ingresado \n")


def eliminar():
    archivo = open("alumnos.txt", "r")
    alu = archivo.readlines()
    archivo.close()
    a = []
    dato = input("Ingrese el dato a eliminar: ")
    for al in alu:
        if not dato in al:
            a.append(al)
    archivo = open("alumnos.txt", 'w')
    archivo.write(a)
    archivo.close()
    print("El elemento ha sido eliminado")


def modificar(alumnos):
    dato = int(input("Ingrese el indice a modificar: "))
    print(alumnos[dato])
    print("Es este el dato a modificar? S/N")
    resp = input("->")
    resp = resp.upper()
    if resp == "S":
        alumnos.pop(dato)
        modif = input("Ingrese el dato corregido: ")
        modif = modif.title()
        alumnos.append(modif)
        print("El dato corregido ha sido guardado")
    else:
        print("No se corrigió ningún dato")
    
def consultar(alumnos):
    archivo = open("alumnos.txt", "r")
    alumnos = archivo.readlines()
    archivo.close()
    cont = 0
    dato = input("Ingrese el dato a buscar: ")
    for al in alumnos:
        if dato.lower() in al.lower():
            print(f"Indice {cont}" + ": " + al)
        cont+=1    

def listado():
	cont = 0
	archivo = open("alumnos.txt", "r")
	alu = archivo.readlines()
	archivo.close()
	for al in alu:
		print(f"Indice {cont}" + ": " + al)
		cont+=1
	print("Listado completo")


while(True):
    print("Elija una opción")
    print("1 - Agregar Alumno")
    print("2 - Eliminar alumno")
    print("3 - Modificar alumno")
    print("4 - Consultar alumno")
    print("5 - Ver listado de alumnos")
    print("6 - Salir")
    op = ""
    while op not in ("1", "2", "3", "4", "5", "6"):
        op = input("-> ")
        if op == "1":
            agregar(alumnos)
        elif op == "2":
            eliminar()
        elif op == "3":
            modificar(alumnos)
        elif op == "4":
            consultar(alumnos)
        elif op == "5":
            listado()
        elif op == "6":
            exit()

        
    

