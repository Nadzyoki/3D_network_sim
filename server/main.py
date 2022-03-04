from ursinanetworking import*

ADDRESS = ("localhost", 25565)

class Server:
    def __init__(self, address) -> None:
        self.ursinaServer = UrsinaNetworkingServer(*address)
        self.start_events_processing_thread()

        @self.ursinaServer.event
        def onClientConnected(Client):
            Client.send_message("HelloFromServer", f"Hello {Client} how are you ?! :D")

        @self.ursinaServer.event
        def messageFromClient(client,cont):
            print(f"{client} say: {cont}")

    def start_events_processing_thread(self):
        def process_net_events():
            while True:
                self.ursinaServer.process_net_events()
        self.processEventsThread = threading.Thread(target=process_net_events)
        self.processEventsThread.start()

if __name__ == "__main__":
    Server = Server(ADDRESS)

