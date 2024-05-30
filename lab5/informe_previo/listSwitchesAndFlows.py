#!/usr/bin/python
import requests
from prettytable import PrettyTable

# DEFINE VARIABLES
controller_ip = '10.20.12.230'  # UNCOMMENT AND EDIT THIS
target_api = '/wm/core/controller/switches/json'  # UNCOMMENT AND EDIT THIS
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
url = f'http://{controller_ip}:8080/{target_api}'
response = requests.get(url=url, headers=headers)

if response.status_code == 200:
    # SUCCESSFUL REQUEST
    print('SUCCESSFUL REQUEST | STATUS: 200')
    data = response.json()
    table = PrettyTable(data[0].keys())
    for row in data:
        table.add_row(row.values())
    print(table)
    switch_dpid = input('Enter DPID:')
    show_flows = f'/wm/core/switch/{switch_dpid}/flow/json'
    flow_url = f'http://{controller_ip}:8080/{show_flows}'
    response = requests.get(url=flow_url, headers=headers)

    if response.status_code == 200:
        # SUCCESSFUL REQUEST
        print('SUCCESSFUL REQUEST | STATUS: 200')
        flows = response.json()

        # Crear una tabla con PrettyTable
        table = PrettyTable()
        table.field_names = ["Version", "Cookie", "Table ID", "Packet Count", "Byte Count", "Duration (s)", "Priority",
                             "Idle Timeout", "Hard Timeout", "Flags", "Actions"]

        # Agregar filas a la tabla
        for flow in flows.get('flows', []):
            actions = flow['instructions']['instruction_apply_actions']['actions']
            table.add_row([
                flow.get('version', ''),
                flow.get('cookie', ''),
                flow.get('tableId', ''),
                flow.get('packetCount', ''),
                flow.get('byteCount', ''),
                f"{flow.get('durationSeconds', '')}.{flow.get('durationNSeconds', '')}",
                flow.get('priority', ''),
                flow.get('idleTimeoutSec', ''),
                flow.get('hardTimeoutSec', ''),
                flow.get('flags', ''),
                actions
            ])
        print(table)
    else:
        # FAILED REQUEST
        print(f'FAILED REQUEST | STATUS: 200 {response.status_code}')


else:
    # FAILED REQUEST
    print(f'FAILED REQUEST | STATUS: 200 {response.status_code}')

# FOR QUESTION 1h COMPLETE FOR PRINT ALL FLOWS PER SWITCH PID FIRST YOU NEED TO ASK USER INPUT A SWITCH PID
# AFTERWARD, BY USING THIS SWITCH PID, YOU SHOULD ASK THE PERTINENT API FOR GET ALL FLOWS PER SWITCH PID AND PRINT
# THEM (AS ABOVE CODE)
