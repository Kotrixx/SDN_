from lab5.informe_final.utils import cursos_crud, alumno_crud
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
                    cursos_crud(data)
                else:
                    print("Importe la data primero\n")
            case "4":
                if data is not None:
                    """cursos = listar_alumnos(data)
                    for i in cursos:
                        print(f"{i['nombre']}")"""
                    alumno_crud(data)

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
