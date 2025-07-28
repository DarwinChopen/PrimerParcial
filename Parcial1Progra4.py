while True:
    print("Menu")
    print("1. Ingreso de datos")
    print("2. Listado Empleados")
    print("3. Mostrar Cuantos Empleados tieen Evaluacion Satisfactoria")
    print("4. Que empleado  tiene el mejor promedio General")
    print("5. Salir")
    try:
        opcion=int(input("Ingrese una opcion..."))
    except ValueError:
        print("Ingrese un entero Positico")
    match opcion:
        case 1:
            print("Ingreso de Empleados")
        case 2:
            print("Datos de emleados")
        case 3:
            print("empleados Evaluacion Satisfactoria")
        case 4:
            print("Empleado con mejor promedio")
        case 5:
            print("Saliedo...")
            break
        case _:
            print("Opcion Invalida intentelo de nuevo")


