import socket
import json


class Client:
    def __init__(self):
        pass

    def connect(self,addr,port,name,passw):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((addr,port))
            self.send_auth(name,passw)
            ans = self.socket.recv(2048).decode()
            if ans == "done":
                return True
            elif ans == "dont done":
                print('fuck')
                return False
        except ConnectionRefusedError :
            return False

    def send_auth(self, name, passw):
        player_info = {
            "type" : "AUTH",
            "name" : name,
            "passw" : passw,
        }
        player_info_encoded = json.dumps(player_info).encode("utf8")

        try:
            self.socket.send(player_info_encoded)
        except socket.error as e:
            print(e)

    def reciver(self):
        try:
            msg = self.socket.recv(2048)
        except socket.error as e:
            print(e)

        if not msg:
            return None

        msg_decoded = msg.decode("utf8")

        left_bracket_index = msg_decoded.index("{")
        right_bracket_index = msg_decoded.index("}") + 1
        msg_decoded = msg_decoded[left_bracket_index:right_bracket_index]

        msg_json = json.loads(msg_decoded)

        return msg_json
