from ursinanetworking import *

ADDRESS = ("localhost", 25565)

class Client:
    def __init__(self, address) -> None:
        self.ursinaClient = UrsinaNetworkingClient(*address)
        self.start_events_processing_thread()
        self.server_name = "No server"
        self.list_room = []
        @self.ursinaClient.event
        def serverName(name):
            print(f"{name} - name of server")
            self.server_name = name

        # @self.ursinaClient.event
        # def ListRoom(list):
        #     self.list_room=list

    def start_events_processing_thread(self):
        def process_net_events():
            while True:
                self.ursinaClient.process_net_events()
        self.processEventsThread = threading.Thread(target=process_net_events)
        self.processEventsThread.start()

if __name__ == "__main__":
    Client = Client(ADDRESS)