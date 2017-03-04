import socket
import sys

def connect(host, port, user, password):
    data = user + " " + password + "\n"
    #print("Client: {0}".format(data))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(bytes(data, "utf-8"))
    return sock

def send(sock, * commands):
    data = "\n".join(commands) + "\n"
    #print("Client: {0}".format(data), end="")

    sock.sendall(bytes(data, "utf-8"))
    sfile = sock.makefile()
    rline = sfile.readline()
    if ("BOMB_OUT" in rline):
        print("Server: {0}".format(rline))
    return rline

def run(user, password, * commands):
    data = user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()

def subscribe(user, password):
    data = user + " " + password + "\nSUBSCRIBE\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()
