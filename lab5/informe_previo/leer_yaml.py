import yaml


def leer_yaml(filename):
    with open(filename, "r") as archivo:
        data = yaml.safe_load(archivo)
        # yaml.dump(data, outfile, default_flow_style=False)
    return data


def agregar_info(filename, key, input_data):

    data = leer_yaml(filename)
    list_data = data[key]
    list_data.append(input_data)
    d = {'A': 'a', 'B': {'C': 'c', 'D': 'd', 'E': 'e'}}
    with open(filename, 'w') as yaml_file:
        yaml.dump(d, yaml_file, default_flow_style=False)


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


if __name__ == "__main__":
    for servidor in leer_yaml("./datos.yaml").get('servidores', []):
        print(servidor['nombre'])
