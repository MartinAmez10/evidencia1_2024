import datetime
pacientes = []
folio_cita = 0
clave_paciente = 0

while True:
    print("Hola!!! selecciona una opcion del menu (selecciona el numero):")
    print("[1]- Registros de pacientes")
    print("[2]- Programacion de citas")
    print("[3]- Realizacion de citas programadas")
    print("[4]- Consultas y reportes")
    print("[5]- Salir de sistema")
    opcion_menu1 = int(input())

    if opcion_menu1 == 1:
        print("Seleccionaste registros de pacientes")
        folio_cita = folio_cita + 1 #+----------------------------------------------------------------------------------

        clave_paciente = int(input("Ingresa la clave del paciente:\n"))

        fecha_cita = input("Ingresa la fecha de la cita:\n")

        print("Selecciona una opcion de os siguientes turnos:")
        print("[M]- Mañana")
        print("[MED]- Mediodia")
        print("[T]- Tarde")
        turno_cita = str(input()).upper

        print("Se registro el paciente de manera correcta")
        print("Desea ingresar mas pacientes?")
        print("[1]- Si")
        print("[2]- No")
        print("Selecciona el numero:")
        opcion_mas_pacientes = int(input())

        if opcion_mas_pacientes == 1:
            False
        elif opcion_mas_pacientes == 2:
            break

    elif opcion_menu1 == 2:
        print("Seleccionaste programacion de citas")
        #CLAVE DE PACIENTE SE DEBE DE GENERAR EN AUTOMATICO -----------------------------------------------------------------------------
        clave_paciente = clave_paciente + 1

        pri_apellido = str(input("Ingresa el primer apellido:\n"))

        seg_apellido = str(input("Ingresa el segundo apellido:\n"))

        nombre_paciente = str(input("Ingresa el nombre del paciente:\n"))

        fecha_nacimiento_paciente = input("Ingresa la fecha de nacimiento del paciente (MM/DD/YYYY):\n")

    elif opcion_menu1 == 3:
        print("Seleccionaste realizacion de citas programadas")

        folio_cita_programada = int(input("Ingrese el folio de la cita programada:\n"))

        clave_paciente_programada = int(input("Ingrese la clave del paciente programado:\n"))

        hora_actual = datetime.datetime.now()
        print(f"Hora de llegada:{hora_actual}")

        peso_kilos = float(input("Ingrese el peso (Kg) del paciente:\n"))

        estatura_cm = float(input("Ingrese la estatura (cm) del paciente:\n"))

    elif opcion_menu1 == 4:
        while True:
            print("Seleccionaste consultas y reportes\n")

            print("Seleccione como desea consultar la informacion:")
            print("[1]- Reportes de citas")
            print("[2]- Reportes de pacientes")
            print("[3]- Regresar al menu anterior")
            opcion_menu2 = int(input("Ingrese el numero deseado:\n"))

            if opcion_menu2 == 1:
                print("Seleccionaste reportes de citas\n")

                print("Como deseas consultar los reportes de citas:")
                print("[1]- Por periodo")
                print("[2]- Por paciente")
                opcion_menu_reportes = int(input("Ingrese el numero deseado:\n"))

                if opcion_menu_reportes == 1:
                    print("Seleccionaste consulta por periodo\n")
                    #REALIZA LA CONSULTA POR PERIODO
                elif opcion_menu_reportes == 2:
                    print("Seleccionaste consulta por paciente\n")
                    #REALIZA LA CONSULTA POR PACIENTE
            elif opcion_menu2 == 2:
                print("Seleccionaste reportes de pacientes\n")

                print("Seleccione alguna de las siguientes opciones:")
                print("[1]- Listado completo de pacientes")
                print("[2]- Busqueda por clave de paciente")
                print("[3]- Busqueda por apellidos y nombres")
                print("[4]- Regresar al menu anterior")
                opcion_menu_pacientes = int(input("Ingrese el numero deseado:\n"))

                if opcion_menu_pacientes == 1:
                    print("Seleccionaste listado compledo de pacientes\n")
                    #PRESENTA TODOS LOS PACIENTES

                elif opcion_menu_pacientes == 2:
                    print("Seleccionaste busqueda por clave de paciente\n")
                    #BUSCA POR CLAVE DE PACIENTE
                    clave_buscar = int(input("Ingresa la clave del paciente que desea buscar:"))

                elif opcion_menu_pacientes == 3:
                    print("Seleccionaste busqueda por apellidos y nombres")
                    #BUSCA POR APELLIDOS Y NOMBRES
                    nombre_buscar = str(input("Ingresa el nombre del paciente:\n"))
                    primer_apellido_buscar = str(input("Ingresa el primer apellido del paciente:\n"))
                    segundo_apellido_buscar = str(input("Ingresa el segundo apellido del paciente:\n"))

                elif opcion_menu_pacientes == 4:
                    break
                    
            elif opcion_menu2 == 3:
                break

    elif opcion_menu1 == 5:
        print("Saliendo del sistema")
