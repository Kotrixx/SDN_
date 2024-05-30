import requests

host = "10.20.12.230"


def get_attachment_points(mac):
    url = f"http://{host}:8080/wm/device/"
    response = requests.get(url)
    if response.status_code == 200:
        devices = response.json()
        for dev in devices:
            if mac in dev['mac']:
                attachment_points = dev['attachmentPoint']
                if attachment_points:
                    dpid = attachment_points[0]['switchDPID']
                    port = attachment_points[0]['port']
                    return {"dpid": dpid, "port": port}
    return None


def get_route(src_dpid, src_port, dst_dpid, dst_port):
    url = f"http://{host}:8080/wm/topology/route/{src_dpid}/{src_port}/{dst_dpid}/{dst_port}/json"
    response = requests.get(url)
    if response.status_code == 200:
        route_info = response.json()
        path = []
        for hop in route_info:
            switch_dpid = hop['switch']
            port_number = hop['port']['portNumber']
            path.append((switch_dpid, port_number))
        return path
    else:
        print(f"Error: {response.status_code}")
        return None


# Ejemplo de uso
if __name__ == "__main__":
    mac_address = "fa:16:3e:1d:f3:c0"
    attach_points = get_attachment_points(mac_address)

    print("=" * 80)
    if attach_points is not None:
        print(f"Host {mac_address} is connected to {attach_points['dpid']}, Port: {attach_points['port']}")
    else:
        print(f"No se encontró el host {mac_address}")
    print("=" * 80)

    src_dpid = "00:00:02:b3:44:c7:54:47"
    src_port = "1"
    dst_dpid = "00:00:1e:66:eb:b8:b3:40"
    dst_port = "2"
    route = get_route(src_dpid, src_port, dst_dpid, dst_port)

    if route:
        print(f"Route from {src_dpid}:{src_port} to {dst_dpid}:{dst_port}:")
        for switch, port in route:
            print(f"\tSwitch: {switch}\n\tPort: {port}")
    else:
        print(f"Route {src_dpid}:{src_port} - {dst_dpid}:{dst_port} not found")
