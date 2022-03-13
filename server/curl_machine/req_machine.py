import requests


class CURL_MACHINE:
    def __init__(self,serv_ip,auth):
        self.serv_ip = serv_ip
        self.auth = auth

    def Get_ID(self,name):
        req = requests.get('http://' + self.serv_ip + ':3080/v2/projects', auth=self.auth)
        for pr in req.json():
            if pr['name'] == name :
                return pr['project_id']
        return 'None'

    def ID_node(self,name):
        req = requests.get('http://' + self.serv_ip + ':3080/v2/projects/' + self.Get_ID(prj_name) + '/nodes', auth=self.auth)
        for pr in req.json():
            if pr['name'] == name :
                return pr['node_id']
        return 'None'

    def Create_vpc(self,name):
        data = ('{"name": "'+name+'", "node_type": "vpcs", "compute_id": "local"}')
        request=requests.post('http://'+self.serv_ip+':3080/v2/projects/'+self.Get_ID(prj_name)+'/nodes', data=data,auth=self.auth)
        print(request.text)

    def Create_dynamips(self):
        data = '{"symbol": ":/symbols/router.svg", "name": "R1", "properties": {"platform": "c7200", "nvram": 512, "image": "c7200-adventerprisek9-mz.124-24.T5.image", "ram": 512, "slot3": "PA-GE", "system_id": "FTX0945W0MY", "slot0": "C7200-IO-FE", "slot2": "PA-GE", "slot1": "PA-GE",  "idlepc": "0x606e0538", "startup_config_content": "hostname %h\\n"}, "compute_id": "local", "node_type": "dynamips"}'

        response = requests.post('http://'+self.serv_ip+':3080/v2/projects/'+self.Get_ID(prj_name)+'/nodes', data=data,auth=self.auth)
        print(response.text)


    def Start_node(self,name):
        data = '{}'
        response = requests.post(
            'http://'+self.serv_ip+':3080/v2/projects/'+self.Get_ID(prj_name)+'/nodes/'+self.ID_node(name)+'/start',
            data=data, auth=self.auth)
        print(response.text)

    def Stop_node(self,name):
        data = '{}'
        response = requests.post(
            'http://'+self.serv_ip+':3080/v2/projects/'+self.Get_ID(prj_name)+'/nodes/'+self.ID_node(name)+'/stop',
            data=data, auth=self.auth)

    def Delete_node(self,name):
        data = '{}'
        response = requests.delete(
            'http://' + self.serv_ip + ':3080/v2/projects/' + self.Get_ID(prj_name) + '/nodes/' + self.ID_node(name) ,
            data=data, auth=self.auth)


# print(ID_node("R3"))
# Start_node("R3")
# req2 = requests.get('http://'+serv_ip+':3080/v2/projects/'+Get_ID(prj_name)+'/nodes',auth=('admin','admin'))
# print(req2.json())
