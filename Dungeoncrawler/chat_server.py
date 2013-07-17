from mastermind_import import *
from settings import *

import threading

class ServerChat(MastermindServerTCP):
    def __init__(self):
        MastermindServerTCP.__init__(self, 0.5,0.5,10.0)

        self.chat = [None]*scrollback
        self.mutex = threading.Lock()

    def add_message(self, msg):
        self.mutex.acquire()
        self.chat = self.chat[1:] + [msg]
        self.mutex.release()

    def callback_connect          (self                                          ):
        #Something could go here
        return super(ServerChat,self).callback_connect()
    def callback_disconnect       (self                                          ):
        #Something could go here
        return super(ServerChat,self).callback_disconnect()
    def callback_connect_client   (self, connection_object                       ):
        #Something could go here
        return super(ServerChat,self).callback_connect_client(connection_object)
    def callback_disconnect_client(self, connection_object                       ):
        #Something could go here
        return super(ServerChat,self).callback_disconnect_client(connection_object)
    
    def callback_client_receive   (self, connection_object                       ):
        #Something could go here
        return super(ServerChat,self).callback_client_receive(connection_object)
    def callback_client_handle    (self, connection_object, data                 ):
        cmd = data[0]
        if cmd == "introduce":
            self.add_message("Server: "+data[1]+" ist der Lobby beigetreten.")
        elif cmd == "add":
            self.add_message(data[1])
        elif cmd == "update":
            pass
        elif cmd == "leave":
            self.add_message("Server: "+data[1]+" hat die Lobby verlassen.")
        self.callback_client_send(connection_object, self.chat)
    def callback_client_send      (self, connection_object, data,compression=None):
        #Something could go here
        return super(ServerChat,self).callback_client_send(connection_object, data,compression)

if __name__ == "__main__":
    server = ServerChat()
    server.connect(ip,port)
    try:
        server.accepting_allow_wait_forever()
    except:
        #Only way to break is with an exception
        pass
    server.accepting_disallow()
    server.disconnect_clients()
    server.disconnect()
