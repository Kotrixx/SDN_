import yaml


class Alumno:
    def __init__(self, nombre, codigo, direccion_mac):
        self.nombre = nombre
        self.codigo = codigo
        self.direccion_mac = direccion_mac

    def __str__(self):
        return f"Nombre: {self.nombre}, MAC: {self.direccion_mac}"


class Curso:
    def __init__(self, nombre, estado, alumnos, servidores):
        self.nombre = nombre
        self.estado = estado
        self.alumnos = alumnos
        self.servidores = servidores

    def __str__(self):
        lista_alumnos = ", ".join(str(alumno) for alumno in self.alumnos)
        lista_servidores = ", ".join(str(servidor) for servidor in self.servidores)
        return f"Curso: {self.nombre}, Estado: {self.estado}, Alumnos:{lista_alumnos}, Servidores: {lista_servidores}"

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def remover_alumno(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
        else:
            print(f"El alumno {alumno} no existe.")

    def anhadir_servicio(self, servidor):
        self.servidores.append(servidor)


class Servidor:
    def __init__(self, nombre, direccion_ip, lista_servicios):
        self.nombre = nombre
        self.direccion_ip = direccion_ip
        self.lista_servicios = lista_servicios

    def __str__(self):
        servicios = ", ".join(str(servicio) for servicio in self.lista_servicios)
        return f"Nombre: {self.nombre}, Dirección IP: {self.direccion_ip}, Servicios: {servicios}"


class Servicio:
    def __init__(self, nombre, protocolo, puerto):
        self.nombre = nombre,
        self.protocolo = protocolo,
        self.puerto = puerto

    def __str__(self):
        return f"Nombre: {self.nombre}, Protocolo: {self.protocolo}, Puerto: {self.puerto}"


def alumno_representer(dumper, data):
    return dumper.represent_dict({
        'nombre': data.nombre,
        'codigo': data.codigo,
        'mac': data.direccion_mac
    })


# Función para construir un objeto Alumno desde un diccionario
def alumno_constructor(loader, node):
    values = loader.construct_mapping(node)
    return Alumno(**values)


yaml.add_representer(Alumno, alumno_representer)
yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, alumno_constructor)

if __name__ == "__main__":
    servicio1 = Servicio("Web1", "HTTP", "80")
    servicio2 = Servicio("Web segura 1", "HTTPS", "443")
    servicio4 = Servicio("Web segura 2", "HTTPS", "443")
    servidor1 = Servidor("Server1", "127.0.0.1", [servicio1, servicio2])
    servidor2 = Servidor("Server2", "192.168.35.10", [servicio4])
    alumno1 = Alumno("Alumno1", "3A:F4:5B:9D:3C:1A")
    alumno2 = Alumno("Alumno2", "B2:8E:7D:4A:2F:9B")
    curso1 = Curso("Curso1", "activo", [alumno1, alumno2], [servidor1,
                                                            servidor2])
    print(curso1)
    print(servidor1)
    print(servidor2)
    print("==============================================================================")
    curso1.remover_alumno(alumno1)
    curso1.agregar_alumno(Alumno("Alumno3", "3A:F4:5A:2D:4C:2B"))
    curso1.anhadir_servicio(Servicio("Correos", "STMP", 587))
    print(curso1)
