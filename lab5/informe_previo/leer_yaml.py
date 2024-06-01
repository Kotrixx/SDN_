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


# Función para construir un objeto Alumno desde un diccionario
def alumno_constructor(loader, node):
    values = loader.construct_mapping(node)
    return Alumno(**values)




if __name__ == "__main__":
    for servidor in leer_yaml("./datos.yaml").get('servidores', []):
        print(servidor['nombre'])
