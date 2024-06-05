import yaml

from lab5.informe_previo.clases import Alumno


def leer_yaml(filename):
    with open(filename, "r") as archivo:
        data = yaml.safe_load(archivo)
        # yaml.dump(data, outfile, default_flow_style=False)
    return data


def agregar_info(filename, key, input_data):
    data = leer_yaml(filename)

    if key not in data:
        data[key] = []

    list_data = data[key]

    if isinstance(input_data, Alumno):
        list_data.append(input_data)
    else:
        raise ValueError("input_data debe ser una instancia de la clase Alumno")

    data[key] = list_data

    with open(filename, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)
    return data


def agregar_alumno_a_curso(filename, data, codigo_curso, nuevo_alumno):
    for curso in data['cursos']:
        if curso['codigo'] == codigo_curso:
            curso['alumnos'].append(nuevo_alumno)
            with open(filename, 'w') as file:
                yaml.dump(data, file, default_flow_style=False)
            return data
    return None


def listar_cursos(data):
    list = []
    for d in data.get('cursos', []):
        list.append(d)
    return list


def listar_alumnos(data):
    list = []
    for d in data.get('alumnos', []):
        list.append(d)
    return list


def agregar_conexion(filename, data, nombre_conexion, codigo, ip_dst, servicio):
    nueva_conexion = {
        nombre_conexion: [
            {'codigo': codigo},
            {'ip_dst': ip_dst},
            {'servicio': servicio}
        ]
    }

    if 'conexiones' not in data:
        data['conexiones'] = []

    data['conexiones'].append(nueva_conexion)
    with open(filename, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

    return data


def eliminar_conexion(filename, data, nombre_conexion):
    if 'conexiones' in data:
        data['conexiones'] = [conn for conn in data['conexiones'] if nombre_conexion not in conn]

        # Escribir los datos actualizados de vuelta al archivo YAML
        with open(filename, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)

        print(f"Conexión {nombre_conexion} eliminada con éxito.")
    else:
        print(f"No se encontró la conexión {nombre_conexion}.")
    return data


def listar_servidores(data):
    list = []
    for d in data.get('servidores', []):
        list.append(d)
    return list


def alumno_representer(dumper, data):
    return dumper.represent_dict({
        'nombre': data.nombre,
        'codigo': data.codigo,
        'direccion_mac': data.direccion_mac
    })


def listar_conexiones(data):
    list = []
    for d in data.get('conexiones', []):
        list.append(d)
    return list


# Función para construir un objeto Alumno desde un diccionario
def alumno_constructor(loader, node):
    values = loader.construct_mapping(node)
    return Alumno(**values)


if __name__ == "__main__":
    for servidor in leer_yaml("./datos.yaml").get('servidores', []):
        print(servidor['nombre'])
