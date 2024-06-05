from lab5.informe_previo.clases import Alumno
from lab5.informe_previo.leer_yaml import listar_cursos, listar_alumnos, agregar_info, listar_conexiones, \
    listar_servidores, agregar_alumno_a_curso, agregar_conexion, eliminar_conexion


def cursos_crud(data):
    while True:
        cursos = listar_cursos(data)
        list_alumnos = []
        action = input("Ingrese la acción a realizar (listar, agregar, detalle, terminar):")
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
        if action == "agregar":
            # verificar si existe
            codigo_curso = input("Ingrese el codigo del curso al que desea agregarle un alumno: ")

            codigo_alumno_input = input("Ingrese el codigo del alumno que desea agregar: ")
            cursos_info = listar_cursos(data)
            curso_seleccionado = None
            for i in cursos_info:
                if i['codigo'] == codigo_curso:
                    curso_seleccionado = i
                    break
            # print(curso_seleccionado)
            # print(curso_seleccionado['alumnos'])
            # print(codigo_alumno_input)
            if int(codigo_alumno_input) not in curso_seleccionado['alumnos']:
                # podria validarse que el alumno exista
                agregar_alumno_a_curso("./database.yaml", data, codigo_curso, int(codigo_alumno_input))
            else:
                print("El alumno ya existe")
        if action == "terminar":
            break


def alumno_crud(data):
    while True:
        alumnos = listar_alumnos(data)
        list_alumnos = []
        action = input("Ingrese la acción a realizar (listar, agregar, terminar):")
        if action == "listar":
            for i in alumnos:
                if isinstance(i, Alumno):
                    print(f"{i.nombre} - {i.codigo} - {i.direccion_mac}")
                else:
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


def conexion_crud(data):
    while True:
        conexiones = listar_conexiones(data)
        servidores = listar_servidores(data)
        list_alumnos = []
        action = input("Conexiones: \nIngrese la acción a realizar (listar, agregar, terminar, eliminar):")
        if action == "listar":
            if conexiones is not None:
                for i in conexiones:
                    print(f"{i['nombre']} - {i['codigo']} - {i['mac']}")
            else:
                print("No hay conexiones")
        if action == "agregar":
            print(f"Ha escogido agregar, ingrese la IP del host")
            # Jacob Astor - 19121404
            cod = 19121404
            ip_dst = input("IP: ")
            # print(servidores)
            for i in servidores:
                servicio_x_usar = None
                if ip_dst == i['ip']:
                    # print(ip_dst)
                    servidor_objetivo = i
                    servicio = input("Ingrese el nombre del servicio: ")
                    # print(servidor_objetivo['servicios'])
                    for j in servidor_objetivo['servicios']:
                        if j['nombre'] == servicio:
                            servicio_x_usar = j['nombre']

                    # chequear si el usuario pertenece al grupo que puede ver el servicio (tel354)
                    curso_cod = verificar_pertenencia_curso(data, cod)
                    if curso_cod is not None:
                        list_cursos = listar_cursos(data)
                        for k in list_cursos:
                            for m in k['servidores']:
                                for n in m['servicios_permitidos']:
                                    if n == servicio_x_usar:
                                        nombre_conexion = "conn" + str(cod)
                                        if not conexion_existe(data, nombre_conexion):
                                            print("Conexion establecida")
                                            data = agregar_conexion("./database.yaml", data, nombre_conexion,
                                                                    cod, ip_dst, servicio_x_usar)
                                        else:
                                            print(f"La conexión ya existe.")
                                        return data
                    else:
                        print("No tiene permiso para acceder a este servicio.")
                        return data
                else:
                    print(f"No se puede establecer conexión con el host {ip_dst} o no existe.")
                    return data
        if action == "eliminar":
            print("Ha escogido eliminar una conexión")
            cod = 19121404
            nombre_conexion = "conn" + str(cod)
            if conexion_existe(data, nombre_conexion):
                data = eliminar_conexion("./database.yaml", data, nombre_conexion)
            else:
                print(f"La conexión {nombre_conexion} no existe.")

        if action == "terminar":
            break

    return data


def verificar_pertenencia_curso(data, cod):
    pertenece_a_curso = False
    for curso in listar_cursos(data):
        for alumno_cod in curso['alumnos']:
            if cod == alumno_cod:
                print(f"Pertenece a {curso['codigo']}")
                return curso['codigo']
        if pertenece_a_curso:
            break
    if not pertenece_a_curso:
        print("No pertenece a ningun curso.")
        return None


def conexion_existe(data, nombre_conexion):
    if 'conexiones' in data:
        for conexion in data['conexiones']:
            if nombre_conexion in conexion:
                return True
    return False


def servidor_crud(data):
    while True:
        servidores = listar_servidores(data)
        list_alumnos = []
        action = input("Servidor: \nIngrese la acción a realizar (listar, agregar, ver permisos):")
        if action == "listar":
            if servidores is not None:
                for i in servidores:
                    ip = i['ip']
                    print(f"\t{i['nombre']}")
                    print(f"\t{ip}")
                    print(f"\t{i['servicios']}")
                    if ip == "10.0.0.3":
                        print("La IP corresponde a h3")
            else:
                print("No hay conexiones")
        if action == "ver permisos":
            server_exists = None
            input_server = input("Ingrese el servidor que desea ver: ")
            for i in listar_servidores(data):
                if input_server == i['nombre']:
                    server_exists = True
                else:
                    server_exists = False
            if server_exists is True:
                input_service = input("Ingrese el servicio: ")
                permitidos = buscar_servidor_y_servicio(data, input_server, input_service)
                if len(permitidos) > 0:
                    print(f"Pueden acceder: ")
                    for i in permitidos:
                        print(f"- {i}")
                else:
                    print("No hay curso con permiso a este servidor-servicio")
            # asd
            else:
                print("No existe el servidor")
        if action == "terminar":
            break

    return data


def buscar_servidor_y_servicio(data, servidor, servicio):
    cursos = listar_cursos(data)
    lista_permitido = []

    for i in cursos:
        cond1 = False
        cond2 = False
        for j in i['servidores']:
            if servidor == j['nombre']:
                cond1 = True
            for k in j['servicios_permitidos']:
                if servicio == k:
                    cond2 = True
            if cond1 and cond2:
                lista_permitido.append(i['codigo'])

    return lista_permitido
