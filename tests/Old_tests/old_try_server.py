# # import socket
# # import asyncio
# # from curl_machine.req_machine import CURL_MACHINE
# #
# # class Server:
# #     def __init__(self, address_self,address_gns):
# #         self.socket = socket.socket(
# #             socket.AF_INET,
# #             socket.SOCK_STREAM,
# #         )
# #         self.main_loop = asyncio.new_event_loop()
# #         self.users = []
# #         self.us_dic = {}
# #         self.address = address_self
# #         self.gns = address_gns
# #         self.server_name="main"
# #
# #     def set_up(self):
# #         self.socket.bind(self.address)
# #         self.socket.listen(5)
# #         self.socket.settimeout(0)
# #         self.socket.setblocking(False)
# #
# #     async def send_data_all(self,data):
# #         for user in self.users:
# #             await self.main_loop.sock_sendall(user, data)
# #
# #     async def send_data_user(self,data,user):
# #         await self.main_loop.sock_sendall(user,data)
# #
# #     async def selector(self,data,user):
# #         def CMN(name):
# #             self.us_dic[user] = name[1]
# #             print(f"{user} change name on {name[1]}")
# #
# #         n_data = data.decode('utf-8').split()
# #
# #         match n_data[0]:
# #             case 'CMN':
# #                 CMN(n_data)
# #             case 'WMN':
# #                 await self.send_data_user(self.us_dic[user].encode('utf-8'), user)
# #             case 'MAU':
# #                 # data_r = data.decode('utf-8').translate({ord(i): None for i in 'MAU'})
# #                 data_r = data.decode('utf-8').replace('MAU ','',1)
# #                 await self.send_data_all((str(self.us_dic[user])+" : "+data_r).encode('utf-8'))
# #             case 'WSN':
# #                 print("whats server name?")
# #                 await self.send_data_user(('NOS '+self.server_name).encode('utf-8'),user)
# #
# #
# #     async def listen_socket(self, listened_socket=None):
# #         if not listened_socket:
# #             return
# #
# #         while True:
# #             data = await self.main_loop.sock_recv(listened_socket, 2048)
# #             await self.selector(data,listened_socket)
# #
# #     async def accept_socket(self):
# #         while True:
# #             user_socket, address = await self.main_loop.sock_accept(self.socket)
# #             print(f"User {address} connect")
# #             self.us_dic[user_socket] = "name"
# #             self.users.append(user_socket)
# #             self.main_loop.create_task(self.listen_socket(user_socket))
# #
# #     async def main(self):
# #         await self.main_loop.create_task(self.accept_socket())
# #
# #     def start(self):
# #         self.main_loop.run_until_complete(self.main())
# #
# # if __name__ == "__main__":
# #     server = Server(('127.0.0.1',1234),('127.0.0.1'))
# #     server.set_up()
# #     server.start()
# import socket
# import threading
#
#
# class ClientThread(threading.Thread):
#     def __init__(self, clientAddress, clientsocket,main):
#         threading.Thread.__init__(self)
#         self.csocket = clientsocket
#         self.server = main
#         self.name = "Noname"
#         print("?????????? ??????????????????????: ", clientAddress)
#
#     def run(self):
#         while True:
#             data = self.csocket.recv(4096)
#             msg = data.decode('utf-8')
#             print(msg)
#
#             if msg == '':
#                 print("????????????????????")
#                 break
#             else:
#                 ans = self.server.selector(msg,self)
#                 if ans:
#                     self.csocket.sendall(ans.encode('utf-8'))
#                     print(f'send {ans}')
#
#
# class Server:
#     def __init__(self,address):
#         # LOCALHOST = "127.0.0.1"
#         # PORT = 1234
#
#         server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#         server.bind(address)
#         print("???????????? ??????????????!")
#         self.server_name = "MAIN server"
#
#
#         while True:
#             server.listen(1)
#             clientsock, clientAddress = server.accept()
#             newthread = ClientThread(clientAddress, clientsock,self)
#             newthread.start()
#
#     def selector(self, data, user):
#         n_data = data.split()
#
#         match n_data[0]:
#             case 'CMN':
#                 user.name = n_data[1]
#                 return ('IMS '+'succes change name')
#             case 'WMN':
#                 return ('IMS '+'your name '+user.name)
#             case 'WSN':
#                 return ('SN '+self.server_name)
#
#         return None
#
# if __name__ == "__main__":
#     ADDRESS = ("127.0.0.1", 1234)
#     server = Server(ADDRESS)
