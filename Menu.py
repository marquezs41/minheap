import Logic as Logic
from Logic import *

def menu(espera):
    
    if espera == 1:
       genero = input("Presione ENTER para continuar ")

    print("Bienvenido al sistema de gestión ypriorización de pacientes en una sala de urgencias.")
    print("1. Registrar paciente")
    print("2. Consultar paciente próximo a atención")
    print("3. Atender siguiente")
    print("4. Consultar pacientes que están en espera en general")
    print("5. Consultar pacientes que están en espera por triaje")
    print("6. Eliminar paciente")
    print("7. Salir")
    
    opcion = input("Por favor, ingresa el número de la opción que deseas realizar: ")
    return opcion

def main():
    ingreso = 0
    tree = min_heap()
    tree.insert(Paciente(12233,'hombre','Pedro',67,4))
    tree.insert(Paciente(12345,'mujer','Teresa',45,2))
    tree.insert(Paciente(45678,'mujer','Sofia',15,4))
    tree.insert(Paciente(56689,'mujer','Ana',45,3))
    tree.insert(Paciente(56789,'mujer','Cecilia',25,2))
    tree.insert(Paciente(78900,'mujer','Andrea',18,2))
    tree.insert(Paciente(89012,'hombre','Jorge',47,3))
    tree.insert(Paciente(90123,'mujer','Alejandra',21,3))
    tree.insert(Paciente(23445,'mujer','Susana',10,1))
    tree.insert(Paciente(34546,'homre','Julio',75,1))
    tree.insert(Paciente(32456,'mujer','Antonia',29,4))
    tree.insert(Paciente(54678,'mujer','Leonor',76,3))
    
    while True:
        opcion = menu(ingreso)
        ingreso = 1

        if opcion == "1":
            id_paciente = int(input("Ingrese el ID del paciente: "))
            genero = input("Ingrese genero del paciente: ")
            nombre = input("Ingrese el nombre del paciente: ")
            edad = int(input("Ingrese la edad del paciente: "))
            triaje = int(input("Ingrese el triaje necesario para el paciente: "))
            paciente = Paciente(id_paciente, genero, nombre, edad, triaje)
            tree.insert(paciente)
            
        elif opcion == "2":
            print("El próximo paciente a atender es:")
            tree.proximoPaciente()
            
        elif opcion == "3":
           tree.atender()
            
        elif opcion == "4":
            print("Pacientes en espera:")
            tree.print_recursivo(tree.root, 0)
            
        elif opcion == "5":
            triaje = int(input("Ingrese el triaje que desea consultar (1-5): "))
            tree.consulta_Triaje(triaje)
            
        elif opcion == "6":
            sub_opcion = input("Eliminar por (1) ID o (2) Nombre: ")
            if sub_opcion == "1":
                id_paciente = int(input("Ingrese el ID del paciente a eliminar: "))
                tree.eliminarPaciente_id(id_paciente)
            elif sub_opcion == "2":
                nombre = input("Ingrese el nombre del paciente a eliminar: ")
                tree.eliminarPaciente_nombre(nombre)
            else:
                print("Opción no válida para eliminar.")
            
        elif opcion == "7":
            print("¡Muchas gracias por visitarnos, espero le hayamos ayudado. Hasta luego, queremos verlo pronto!")
            break
    
        else:
            print("Opción no válida. Por favor, ingresa una opción válida.")

if __name__ == "__main__":
    main()

            
