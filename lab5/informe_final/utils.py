from lab5.informe_previo.clases import Alumno
from lab5.informe_previo.leer_yaml import listar_cursos, listar_alumnos, agregar_info


def cursos_crud(data):
    while True:
        cursos = listar_cursos(data)
        list_alumnos = []
        action = input("Ingrese la acción a realizar (listar, actualizar, detalle, terminar):")
        if action == "listar":
            for i in cursos:
                print(f"{i['nombre']} - {i['estado']}")
        if action == "detalle":
            curs = input("Ingrese el nombre del curso a detallar (codigo): ")
            for i in cursos:
                if i['codigo'] == curs:
                    print(f"{i['nombre']}({i['codigo']}) - {i['estado']}:")
                    print(f"Alumnos:")
                    for alumno in i['alumnos']:
                        print(f"\t{alumno}")
                    print(f"Servidores:")
                    for servidor in i['servidores']:
                        print(f"\t{servidor['nombre']} - {servidor['servicios_permitidos']}")
        if action == "actualizar":
            dict_alumnos = {}
            num = 1

            print(f"Ha escogido actualizar, ingrese el alumno "
                  f"(en caso ya exista lo eliminará y en caso no, lo creará)")
            for i in cursos:
                dict_alumnos["curso" + str(num)] = i["alumnos"]
                num = num + 1

            print(dict_alumnos)

            codigo = input("Codigo: ")

            if codigo in list_alumnos:
                print("existe")
            else:
                print("no existe")

        if action == "terminar":
            break


def alumno_crud(data):
    while True:
        alumnos = listar_alumnos(data)
        list_alumnos = []
        action = input("Ingrese la acción a realizar (listar, agregar, terminar):")
        if action == "listar":
            for i in alumnos:
                print(f"{i['nombre']} - {i['codigo']} - {i['mac']}")
        if action == "agregar":
            print(f"Ha escogido agregar, ingrese los datos del alumno (nombre, codigo, mac)")

            codigo = input("Codigo: ")
            nombre = input("Nombre: ")
            mac = input("mac: ")
            alumno = Alumno(nombre, codigo, mac)
            if codigo in list_alumnos:
                print("El alumno ya existe en la lista")
            else:
                data = agregar_info("./database.yaml", "alumnos", alumno)
        if action == "terminar":
            break

    return data
