import socket
import asyncio

class Client:
    def __init__(self,address):
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )
        self.main_loop = asyncio.new_event_loop()
        self.address = address
        self.server_name='ans client'
        self.sended = 'NO'

    def set_up(self):
        self.socket.connect(self.address)
        self.socket.setblocking(False)

    async def selector(self,data):
        n_data = data.decode('utf-8').split()

        match n_data[0]:
            case 'NOS':
                self.server_name = n_data[1]
                print(f"server name {n_data[1]}")

    async def listen_socket(self):
        while True:
            data = await self.main_loop.sock_recv(self.socket, 2048)
            print(data.decode('utf-8'))
            await self.selector(data)


    async def send_data(self):
        while True:
            if not(self.sended == 'NO'):
                await self.main_loop.sock_sendall(sock=self.socket,data=self.sended.encode("utf-8"))

    def WSN(self):
        self.main_loop.create_task(self.main_loop.sock_sendall(self.socket,'WSN'.encode('utf-8')))

    async def main(self,win):
        await asyncio.gather(
            self.main_loop.create_task(self.listen_socket()),
            #self.main_loop.create_task(self.send_data()),
            self.main_loop.create_task(win.run())
        )

    def start(self,win):
        self.main_loop.run_until_complete(self.main(win))

