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
            empleados={}
            cantidad=int(input("Ingrese la cantidad de Empleados que desea ingresar"))
            for i in range(cantidad):

                while True:
                    codigo=input("Ingrese el codigo del empleado")
                    if codigo in empleados:
                        print("Este codigo ya existe")
                    else:
                        break
                empleados[codigo]={}
                empleados[codigo]["Nombre"]=input("Ingrese el nombre del empleado")
                empleados[codigo]["Departamento"]=input("Ingrese el Departamento")
                empleados[codigo]["Antiguedad"]=int(input("Ingrese sus años de antiguedad"))
                empleados[codigo]["Telefono"]=int(input("Ingrese el telefono"))
                empleados[codigo]["Correo"]=input("Ingrese el correo")
                empleados[codigo]["Evaluacion"]={}
                cantidad_Evaluaciones = int(input("¿A Cuantas Evaluaciones realizara? "))
                for j in range(cantidad_Evaluaciones):
                    codigo_Evaluacion = input("Ingrese el Codigo de Evaluacion: ")
                    empleados[codigo]["Evaluacion"][codigo_Evaluacion] = {

                    }
                    puntualidad=int("Ingrese la puntualidad")
                    equipo=int("Ingrese elm trabajo en equipo")
                    productividad=int("Ingrese productividad")
                    observaciones=int("Ingrese las observaciones")
                    promedio=int("Ingrese el promedio")
                    estado=input("Ingrese su estado")
                    empleados[codigo]["Evaluacion"][codigo_Evaluacion] ={
                        "puntualidad":puntualidad,
                        "equipo":equipo,
                        "productividad":productividad,
                        "observaviones":observaciones,
                        "Promedio":promedio,
                        "estado":estado
                    }
        case 2:
            print("Datos de emleados")
            for codigo_Evaluacion, datos in empleados.items():
                print(f"Codigo empleado: {codigo}")
                print(f"Nombre: {datos['nombre']}")
                print(f"Departemento: {datos['Departamento']}")
                print(f"Antiguedad: {datos['Antiguedad']}")
                print(f"Telefono: {datos['Telefono']}")
                print(f"Correo: {datos['Correo']}")

        case 3:
            print("empleados Evaluacion Satisfactoria")
        case 4:
            print("Empleado con mejor promedio")
        case 5:
            print("Saliedo...")
            break
        case _:
            print("Opcion Invalida intentelo de nuevo")




