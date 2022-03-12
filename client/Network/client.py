import socket
import asyncio
from os import system


class Client:
    def __init__(self,address):
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )
        self.main_loop = asyncio.new_event_loop()
        self.address = address
        self.message = []
        self.server_name='ans client'

    def set_up(self):
        self.socket.connect(self.address)
        self.socket.setblocking(False)

    async def listen_socket(self):
        while True:
            data = await self.main_loop.sock_recv(self.socket, 2048)
            # self.message.append(data.decode("utf-8"))
            # system('cls')
            # for i in self.message :
            #     print(i)
            print(data.decode('utf-8'))

    async def send_data(self):
        while True:
            data = await self.main_loop.run_in_executor(None,input,' ')
            await self.main_loop.sock_sendall(self.socket,data.encode("utf-8"))

    async def main(self,win):
        await asyncio.gather(
            self.main_loop.create_task(self.listen_socket()),
            self.main_loop.create_task(self.send_data()),
            self.main_loop.create_task(win.run())
        )

    def start(self,win):
        self.main_loop.run_until_complete(self.main(win))

