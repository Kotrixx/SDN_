from lab5.informe_previo.clases import Alumno
from lab5.informe_previo.leer_yaml import leer_yaml, listar_cursos, listar_alumnos, listar_servidores

data = None

if __name__ == "__main__":
    while True:
        print(f"#################################################################\n"
              f"Network Policy manager PUCP-L5\n"
              f"#################################################################"
              f"\nSeleccione una opción:"
              f"\n1) Importar"
              f"\n2) Exportar"
              f"\n3) Cursos"
              f"\n4) Alumnos"
              f"\n5) Servidores"
              f"\n6) Políticas"
              f"\n7) Conexiones"
              f"\n8) Salir")
        option = input(">>>")

        match option:
            case "1":
                data = leer_yaml("./database.yaml")
                print("Data importada correctamente")
                print(data)
            case "3":
                if data is not None:
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
                                dict_alumnos["curso"+str(num)] = i["alumnos"]
                                num = num + 1

                            print(dict_alumnos)

                            codigo = input("Codigo: ")

                            if codigo in list_alumnos:
                                print("existe")
                            else:
                                print("no existe")

                        if action == "terminar":
                            break

                else:
                    print("Importe la data primero\n")
            case "4":
                if data is not None:

                    cursos = listar_alumnos(data)
                    for i in cursos:
                        print(f"{i['nombre']}")
                else:
                    print("Importe la data primero\n")

            case "5":
                print("Servidores:")
                if data is not None:
                    cursos = listar_servidores(data)
                    for i in cursos:
                        ip = i['ip']
                        print(f"\t{i['nombre']}")
                        print(f"\t{ip}")
                        print(f"\t{i['servicios']}")
                        if ip == "10.0.0.3":
                            print("La IP corresponde a h3")
                else:
                    print("Importe la data primero\n")

            case _:
                print("Incorrecto")
