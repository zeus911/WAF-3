__author__ = 'Raul'

import socket
import select
import Security

class Proxy:

    def __init__(self, host, port):

        self.server = None
        self.startproxy(host, port)

        self.read = []
        self.comunication = {}
        self.running = 1
        self.data = None

        self.htmlXSS = open('HTML/XSS.html', 'r').read()
        self.htmlSQL = open('HTML/SQLInjection.html', 'r').read()

    def startproxy(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(0)

    def start(self):
        self.read.append(self.server)
        while self.running:

            entradas, salidas, error = select.select(self.read, [], [])
            for self.input_socket in entradas:

                if self.input_socket is self.server:
                    self.aceptconection()
                    break

                self.data = self.input_socket.recv(4096)

                if len(self.data) is 0:
                    self.closeconection()
                    break
                else:

                    Security.HTTP(self.data).getparam()
                    #detect = Security.Request(self.data).analyzevalues()
                    #if detect is True:
                    self.sendmessage()
                    #elif detect == 'Attack SQLInjection':
                    #    self.input_socket.send(self.htmlSQL)
                    #    self.closeconection()
                    #elif detect == 'Attack XSS':
                    #    self.input_socket.send(self.htmlXSS)
                    #    self.closeconection()

    def closeconection(self):
        conn = self.comunication[self.input_socket]

        self.comunication[conn].close()
        self.comunication[self.input_socket].close()

        self.read.remove(self.input_socket)
        self.read.remove(conn)

        del self.comunication[conn]
        del self.comunication[self.input_socket]

    def sendmessage(self):
        self.comunication[self.input_socket].send(self.data)

    def aceptconection(self):

        self.http = self.getserverconection()

        if self.http:
            self.client_socket, address_client = self.server.accept()
            self.read.append(self.client_socket)
            self.read.append(self.http)
            self.comunication[self.client_socket] = self.http
            self.comunication[self.http] = self.client_socket

    def getserverconection(self):
        try:
            serverhttp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverhttp.connect(('localhost', 80))
            return serverhttp
        except Exception:
            return None

