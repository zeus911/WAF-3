import Proxy


def main():
    ip = 'localhost'
    port = 9090
    print "Inicio del proxy"
    server = Proxy.Proxy(ip, port)
    print "Servidor proxy iniciado en la IP", ip, "y puerto", port
    server.start()

if __name__ == '__main__':
    main()
