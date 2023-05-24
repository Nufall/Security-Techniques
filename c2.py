import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from AES import *
from elgamal import *
from DES import *
from RSA2 import *
class Client:
    def command1(self):
        # self.client.send('Command 1 was triggered'.encode('utf-8'))
        #self.client.send(self.msg_entry.get().encode('utf-8'))
        print(self.msg_entry.get())
        cc = AESCallEncrypt(self.msg_entry.get(),self.aeskey)
        cc = cc + '1'
        self.client.send(cc.encode('utf-8'))

    def __init__(self, host = '192.168.0.108', port = 55555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.root = tk.Tk()
        self.chat_window = scrolledtext.ScrolledText(self.root,height=15,bg="#87b4dc",fg="white",font=('Arial 13'))
        self.chat_window.pack()
        self.msg_entry = tk.Entry(self.root,width=50, font=('Arial 15'))
        #self.msg_entry.bind("<Return>", self.write)
        self.msg_entry.pack(pady=10)
        self.button1 = tk.Button(self.root, text="AES", command=self.command1,bg="#87b4dc",width=10,fg="white")
        self.button1.pack(pady=10)
        self.button2 = tk.Button(self.root, text="DES", command=self.command2,bg="#87b4dc",width=10,fg="white")
        self.button2.pack(pady=10)
        self.button3 = tk.Button(self.root, text="ELGAMAL", command=self.command3,bg="#87b4dc",width=10,fg="white")
        self.button3.pack(pady=10)
        self.button4 = tk.Button(self.root, text="RSA", command=self.command4,bg="#87b4dc",width=10,fg="white")
        self.button4.pack(pady=10)
        self.aeskey = ''
        self.deskey = ''
        self.stop_thread = False
        self.q = None
        self.public_key_b = None
        self.primitive_root = None
        self.session_key = None
        self.public_key_a = None
        self.n = None
        self.e = None
        self.d = None



    def command2(self):
        print(self.msg_entry.get())
        cc = encrypt(self.msg_entry.get(),self.deskey)
        cc = cc + '2'
        print('Encrypt Key: ', self.deskey)
        self.client.send(cc.encode('utf-8'))


    def command3(self):
        #self.client.send('Command 3 was triggered'.encode('utf-8'))
        cc,self.public_key_a= encryption_elgamal(self.msg_entry.get(),self.q,self.public_key_b,self.primitive_root)
        print('real cipher: ', cc)
        cc = '-'.join(str(x) for x in cc)
        cc = str(self.public_key_a) + '-' + cc + '3'
        print('cc', cc)
        self.client.send(cc.encode('utf-8'))



    def command4(self):
        #self.client.send('Command 3 was triggered'.encode('utf-8'))
        cc = cipherRSA(self.msg_entry.get(),self.n,self.e)
        cc = '-'.join(str(x) for x in cc)
        cc = cc + '4'
        self.client.send(cc.encode('utf-8'))
    def receive_messages(self):
        while not self.stop_thread:
            # try:
            message = self.client.recv(1024).decode('utf-8')

            if message[0:4] =='key:' :
                capsule = message[4:len(message)]
                capsule = (capsule.split('-'))
                kkks = eval(capsule.pop(0))
                print('capsule: ', capsule)
                print('keybig: ',kkks)

                for i, x in enumerate(capsule):
                    capsule[i] = int(x)


                print('keys: ' , self.deskey,self.aeskey)
                self.q = capsule[0]
                self.public_key_b = capsule[1]
                self.primitive_root = capsule[2]
                self.session_key = capsule[3]
                self.n = capsule[4]
                self.e = capsule[5]
                self.d = capsule[6]
                self.public_key_a = capsule[7]
                print('capsule: ', capsule)
                keybig = decryption_elgamal(kkks, self.public_key_a, self.session_key, self.q)
                print('keybig ',keybig[0])

                for x in keybig:
                    self.deskey +=x
                #self.deskey = str(keybig)
                self.aeskey = self.deskey[0:16]
                print('Received Key: ', self.deskey)
            else:
                print('entered')
                ddd = ''
                holder = message
                print('holdeR: ', holder)
                if holder[-1] == '1':
                    ddd = AESCallDecrypt(holder[0:len(holder) - 1], self.aeskey)
                elif holder[-1] == '2':

                    ddd = decrypt((holder[0:len(holder) - 1]), self.deskey)
                    print('des: ', ddd)


                elif holder[-1] == '3':
                    cc = [int(x) for x in holder[0:len(holder) - 1].split('-')]
                    print('ddd: ', cc)
                    self.public_key_a = cc.pop(0)
                    print('dejoine list: ', cc)
                    #cc is cipher text turned into list
                    listofletters = decryption_elgamal(cc,self.public_key_a,self.session_key,self.q)
                    #joining the letters into a string from a list
                    for x in listofletters:
                        ddd += x
                    print('iwannasee: ', ddd)


                elif holder[-1] == '4':
                    print('ddd: ', holder[0:len(holder) - 1])
                    cc = [int(x) for x in holder[0:len(holder) - 1].split('-')]
                    ddd = decipherRSA(cc,self.n,self.d)

                self.chat_window.insert(tk.END, ddd+"\n")
            # except:
            #     print("An error occurred!")
            #     self.client.close()
            #     break



    # def write(self, event=None):
    #     message = f'{self.msg_entry.get()}'
    #     self.msg_entry.delete(0, tk.END)
    #     self.client.send(message.encode('utf-8'))
    def stop(self):
        self.stop_thread = True
        self.root.quit()
        self.root.destroy()

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.stop)
        threading.Thread(target=self.receive_messages).start()
        self.root.mainloop()

client = Client()
client.run()
