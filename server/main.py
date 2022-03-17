
import socket
import asyncio

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

    def set_up(self):
        self.socket.bind(self.address)
        self.socket.listen(5)
        self.socket.settimeout(0)
        self.socket.setblocking(False)

    async def send_data_all(self,data):
        for user in self.users:
            await self.main_loop.sock_sendall(user, data.encode('utf-8'))

    async def send_data_user(self,data,user):
        await self.main_loop.sock_sendall(user,data.encode('utf-8'))

    async def selector(self,data,user):
        def CMN(name):
            self.us_dic[user] = name
            print(f"{user} сменил имя на {name}")

        n_data = data.decode('utf-8').split()
        match n_data[0]:
            case 'CMN':
                CMN(n_data[1])
            case 'WMN':
                await self.send_data_user(self.us_dic[user], user)
            case 'MAU':
                # data_r = data.decode('utf-8').translate({ord(i): None for i in 'MAU'})
                data_r = data.decode('utf-8').replace('MAU ','',1)
                await self.send_data_all(str(self.us_dic[user])+" : "+data_r)
            case 'WSN':
                await self.send_data_user("SN "+self.server_name, user)
            case 'IDS':
                await self.send_data_user("Goodbye", user)




    async def listen_socket(self, listened_socket=None):
        if not listened_socket:
            return

        while True:
            try:
                data = await self.main_loop.sock_recv(listened_socket, 2048)
                print(f"Клиент ({self.us_dic[listened_socket]}) прислал :{data.decode('utf-8')} ")
                await self.selector(data,listened_socket)
            except ConnectionResetError:
                print(f"{self.us_dic[listened_socket]} отключился")
                self.users.remove(listened_socket)
                self.us_dic.pop(listened_socket)
                break

    async def accept_socket(self):
        while True:
            user_socket, address = await self.main_loop.sock_accept(self.socket)
            print(f"{user_socket} подключился")
            self.us_dic[user_socket] = "name"
            self.users.append(user_socket)
            self.main_loop.create_task(self.listen_socket(user_socket))

    async def main(self):
        await self.main_loop.create_task(self.accept_socket())

    def start(self):
        self.main_loop.run_until_complete(self.main())

if __name__ == "__main__":
    port = int(input('what port '))
    name = input('what server name ')
    ip = input('ip server ')
    server = Server((ip,port),name)
    server.set_up()
    server.start()
