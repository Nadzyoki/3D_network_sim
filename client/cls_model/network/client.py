from ursinanetworking import *

ADDRESS = ("localhost", 25565)

def start_events_processing_thread(client):
    def process_net_events():
        while True:
            client.process_net_events()
    processEventsThread = threading.Thread(target=process_net_events)
    processEventsThread.start()

urClient = UrsinaNetworkingClient(*ADDRESS)
start_events_processing_thread(urClient)

@urClient.event
def HelloFromServer(Content):
    print(f"Server says : {Content}")

@urClient.event
def message(cont):
    urClient.send_message("messageFromClient",cont)

while True:
    mes = str(input())
    message(mes)