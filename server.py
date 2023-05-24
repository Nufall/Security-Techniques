import socket
import threading
import random
from elgamal import *
from RSA2 import *
class Server:
    def __init__(self, host='192.168.0.108', port=55555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.nicknames = []
        self.key = None


    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def genkey(self):

        key = ''.join(random.choice(['0', '1']) for _ in range(64))
        return key



    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f"Connected with {str(address)}")
            #accepting connection
            self.nicknames.append(str(address))
            self.clients.append(client)

            print(f"Client's ID is {str(address)}!")

            if (len(self.nicknames))==1:
                key = self.genkey()
                #generating keys
                q, public_key_b, primitive_root, session_key = starter()

                n, e, d = keygen()
                cc, public_key_a = encryption_elgamal(key, q,public_key_b,
                                                      primitive_root)

                capsule = '-'.join([str(cc), str(q), str(public_key_b), str(primitive_root), str(session_key),str(n),str(e),str(d),str(public_key_a)])

            prvkeys = 'key:' + capsule
            print(str(q), str(public_key_b), str(primitive_root), str(session_key),str(n),str(e),str(d),str(public_key_a))
            #client.send(key.encode('utf-8'))
            client.send(prvkeys.encode('utf-8'))
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

    def run(self):
        print("Server Started!")

        q,public_key_b,primitive_root,session_key = starter()
        self.receive()

server = Server()
server.run()
