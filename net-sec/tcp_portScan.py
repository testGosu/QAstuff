__author__ = 'Maciej'

import argparse
from socket import  *



def showHeader(socket, target_port):
    try:

        if (target_port == 80):
            socket.send("GET HTTP/1.1 \n")

        else:
           socket("\r\n")

        results = socket.recv(4096)

    except:
        print "BUUUUUU Header not available \n"

def scan_connection(host, port):
    try:
        connection_socket = socket(AF_INET, SOCK_STREAM)
        connection_socket.connect((host, port))
        print "#### BINGO    %d port is open" % (port)
        showHeader(connection_socket, port)
    except:
        print "### BUUUUU   %d port closed" %(port)

    finally:
        connection_socket.close()


def scan_ports(host,ports):
    try:
        IP = gethostbyname(host)

    except:
        print "unknown host"
        exit(0)

    try:
        host = gethostbyaddr(host)
        print "##BINGO#    found: " + host[0] + " #### "
    except:
        print "##BINGO#    found: " + IP + "#### "

    setdefaulttimeout(15)

    for port in ports:
        scan_connection(host, int(port))


def main():
    #CLI handler
    parser = argparse.ArgumentParser('TCP scanner')
    parser.add_argument("-addr", type=str, help="Target IP")
    parser.add_argument("-port", type=str, help="port number")
    args = parser.parse_args()

    ipaddr = args.addr
    port = args.port.split(',')

    scan_ports(ipaddr, port)


if __name__ == "__main__":
    main()