import socket
import asyncio
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import json
from werkzeug.security import check_password_hash




# class User(declarative_base):
#     id = Column(Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     email = Column(String(100), unique=True)
#     password = Column(String(100))
#     name = Column(String(1000))


class Server:
    def __init__(self,address,name):
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )
        self.main_loop = asyncio.new_event_loop()
        self.users = []
        self.us_dic = {}
        self.address = address
        self.server_name=name

        # self.sqlite_clients = sqlite3.connect('db/db.sqlite')
        # print(self.sql_passw('Herony'))
        # self.sqlite_clients.close()

        # engine = create_engine('sqlite:///db.sqlite')
        #
        #
        #
        # DBSession = sessionmaker(bind=engine)
        # self.session = DBSession()
        # print(self.session.query(User).filter_by(id=1).first())

    #SQL section
    def sql_passw(self,name):
        sqlite_clients = sqlite3.connect('E:/pycharm/3D_network/web_server/auth/project/db.sqlite')
        cursorObj = sqlite_clients.cursor()
        cursorObj.execute("SELECT password FROM user WHERE name = ?",[(name)])
        ans = cursorObj.fetchall()[0][0]
        print(type(ans))
        sqlite_clients.close()
        return ans


    def sql_ver_name(self,name):
        sqlite_clients = sqlite3.connect('E:/pycharm/3D_network/web_server/auth/project/db.sqlite')
        cursorObj = sqlite_clients.cursor()
        cursorObj.execute("SELECT name FROM user")
        rows = cursorObj.fetchall()
        for row in rows:
            for i in row:
                print(i)
                if i == name:
                    return True
        return False


    def set_up(self):
        self.socket.bind(self.address)
        self.socket.listen(5)
        self.socket.settimeout(0)
        self.socket.setblocking(False)

    async def send_data_all(self,data):
        for user in self.users:
            await self.main_loop.sock_sendall(user, data.encode('utf8'))

    async def send_data_user(self,data,user):
        await self.main_loop.sock_sendall(user,data.encode('utf8'))

    async def selector(self,data,user):
        try:
            msg_decoded = data.decode("utf8")

            left_bracket_index = msg_decoded.index("{")
            right_bracket_index = msg_decoded.index("}") + 1
            msg_decoded = msg_decoded[left_bracket_index:right_bracket_index]

            msg_json = json.loads(msg_decoded)
            match msg_json["type"]:
                case "AUTH":
                    if self.sql_ver_name(msg_json["name"]):
                        if check_password_hash(str(self.sql_passw(msg_json["name"])), msg_json["passw"]):
                            print('done')
                            await self.send_data_user("done", user)
                    else:
                        print('dont done')
                        await self.send_data_user("dont done", user)
        except ValueError:
            await self.send_data_user("Goodbye", user)


        # def CMN(name):
        #     self.us_dic[user] = name
        #     print(f"{user} сменил имя на {name}")
        #
        # n_data = data.decode('utf-8').split()
        # match n_data[0]:
        #     case 'CMN':
        #         CMN(n_data[1])
        #     case 'WMN':
        #         await self.send_data_user(self.us_dic[user], user)
        #     case 'MAU':
        #         # data_r = data.decode('utf-8').translate({ord(i): None for i in 'MAU'})
        #         data_r = data.decode('utf-8').replace('MAU ','',1)
        #         await self.send_data_all(str(self.us_dic[user])+" : "+data_r)
        #     case 'WSN':
        #         await self.send_data_user("SN "+self.server_name, user)
        #     case 'IDS':
        #         await self.send_data_user("Goodbye", user)




    async def listen_socket(self, listened_socket=None):
        if not listened_socket:
            return

        while True:
            try:
                data = await self.main_loop.sock_recv(listened_socket, 2048)

                try:
                    print(f"Клиент ({self.us_dic[listened_socket]}) прислал :{data.decode('utf-8')} ")
                    await self.selector(data,listened_socket)
                except IndexError:
                    print(f"{self.us_dic[listened_socket]} отключился")
                    break
            except ConnectionResetError:
                print(f"{self.us_dic[listened_socket]} отключился")
                self.users.remove(listened_socket)
                self.us_dic.pop(listened_socket)
                break
            except ConnectionAbortedError:
                print(f"{self.us_dic[listened_socket]} отключился")
                self.users.remove(listened_socket)
                self.us_dic.pop(listened_socket)
                break

    async def accept_socket(self):
        while True:
            user_socket, address = await self.main_loop.sock_accept(self.socket)
            print(f"{address} подключился")
            self.us_dic[user_socket] = "name"
            self.users.append(user_socket)
            self.main_loop.create_task(self.listen_socket(user_socket))

    async def main(self):
        await self.main_loop.create_task(self.accept_socket())

    def start(self):
        self.main_loop.run_until_complete(self.main())

if __name__ == "__main__":
    # port = int(input('what port '))
    # name = input('what server name ')
    # ip = input('ip server ')
    server = Server(('127.0.0.1',8000),'main_3d')
    server.set_up()
    server.start()
