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
            print(data.decode('utf-8'))

    async def send_data(self):
        while True:
            data = await self.main_loop.run_in_executor(None,input,' ')
            await self.main_loop.sock_sendall(self.socket,data.encode("utf-8"))

    async def main(self,):
        await asyncio.gather(
            self.main_loop.create_task(self.listen_socket()),
            self.main_loop.create_task(self.send_data()),
        )

    def start(self):
        self.main_loop.run_until_complete(self.main())

if __name__ == "__main__":
    client = Client(('127.0.0.1',1234))
    client.set_up()
    client.start()