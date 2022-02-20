from ursinanetworking import *

ADDRESS = ("localhost", 25565)

class Client:
    def __init__(self,address) -> None:
        self.urClient = UrsinaNetworkingClient(*address)
        self.start_events_processing_thread()

        @self.urClient.event
        def HelloFromServer(Content):
            print(f"Server says : {Content}")
        

    def start_events_processing_thread(self):
        def process_net_events():
            while True:
                self.urClient.process_net_events()

        self.processEventsThread = threading.Thread(target=process_net_events)
        self.processEventsThread.start()




if __name__ == '__main__':
    client = Client(ADDRESS)


    