import requests
from per import *

def Get_ID(name):
    req = requests.get('http://' + serv_ip + ':3080/v2/projects', auth=('admin', 'admin'))
    for pr in req.json():
        if pr['name'] == name :
            return pr['project_id']
    return 'None'

def ID_node(name):
    req = requests.get('http://' + serv_ip + ':3080/v2/projects/' + Get_ID(prj_name) + '/nodes', auth=('admin', 'admin'))
    for pr in req.json():
        if pr['name'] == name :
            return pr['node_id']
    return 'None'

def Create_vpc(name):
    data = ('{"name": "'+name+'", "node_type": "vpcs", "compute_id": "local"}')
    request=requests.post('http://'+serv_ip+':3080/v2/projects/'+Get_ID(prj_name)+'/nodes', data=data,auth=('admin','admin'))
    print(request.text)

def Create_dynamips():
    data = '{"symbol": ":/symbols/router.svg", "name": "R1", "properties": {"platform": "c7200", "nvram": 512, "image": "c7200-adventerprisek9-mz.124-24.T5.image", "ram": 512, "slot3": "PA-GE", "system_id": "FTX0945W0MY", "slot0": "C7200-IO-FE", "slot2": "PA-GE", "slot1": "PA-GE",  "idlepc": "0x606e0538", "startup_config_content": "hostname %h\\n"}, "compute_id": "local", "node_type": "dynamips"}'

    response = requests.post('http://'+serv_ip+':3080/v2/projects/'+Get_ID(prj_name)+'/nodes', data=data,auth=('admin','admin'))
    print(response.text)


def Start_node(name):
    data = '{}'
    response = requests.post(
        'http://'+serv_ip+':3080/v2/projects/'+Get_ID(prj_name)+'/nodes/'+ID_node(name)+'/start',
        data=data, auth=('admin', 'admin'))
    print(response.text)

def Stop_node(name):
    data = '{}'
    response = requests.post(
        'http://'+serv_ip+':3080/v2/projects/'+Get_ID(prj_name)+'/nodes/'+ID_node(name)+'/stop',
        data=data, auth=('admin', 'admin'))

def Delete_node(name):
    data = '{}'
    response = requests.delete(
        'http://' + serv_ip + ':3080/v2/projects/' + Get_ID(prj_name) + '/nodes/' + ID_node(name) ,
        data=data, auth=('admin', 'admin'))

# print(ID_node("R3"))
# Start_node("R3")




# req2 = requests.get('http://'+serv_ip+':3080/v2/projects/'+Get_ID(prj_name)+'/nodes',auth=('admin','admin'))
# print(req2.json())
