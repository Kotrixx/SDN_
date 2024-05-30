import yaml


def leer_yaml(filename):
    with open(filename, "r") as archivo:
        data = yaml.safe_load(archivo)
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


if __name__ == "__main__":
    for servidor in leer_yaml("./datos.yaml").get('servidores', []):
        print(servidor['nombre'])
