
#!/usr/bin/env python3
#PortScanner
#Project By Gabriel #OoMiCaDo
#v1.0.2
import socket
import logging
import datetime


#---------Welcome banner------------

print("-" * 50)
print("                        Port Scanner                            ")
print("                        Version 1.0.2                           ")
print("                  ****Project By Gabriel****                    ")
print("-" * 50)

class PortScanner:

    def __init__(self, type = 'simple', ports = 80, host = '127.0.0.1'):
        self.host = host
        self.type = type
        self.ports = ports
        logging.basicConfig(level=logging.DEBUG,
                    filename=datetime.datetime.now().strftime('%d-%m-%Y.log'),
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')
    
    def setType(self, type = 'simple'):
        self.type = type

    def setPorts(self, ports = 80):
        self.ports = ports

    def scan(self):
        if self.type == "simple":
            logging.info(self.scanSimple(self.ports))
        elif self.type == "range":
            for i in self.ports:
                if isinstance(i, str):
                    result = i.split('-')
                    for j in range(int(result[0]),int(result[1])+1):
                        print(j)
                        logging.info(self.scanSimple(j))
                else:
                    print(i)
                    logging.info(self.scanSimple(i))
        elif self.type == "all":
            self.type = 'range'
            self.ports = ['0-65535']
            self.scan()

    def scanSimple(self,port : int):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        try:
            ip = socket.gethostbyname(self.host)
            sock.connect((ip, port))
            return "Port "+str(port)+" Ouvert "    #Conversion de l'entier port en chaine de caractère 
        except socket.gaierror:
            return 'Unresolved address'
        except ConnectionRefusedError:
            return "Port "+str(port)+"Filtré"
        except socket.timeout:
            return "Port "+str(port)+" Fermé "
        except:
            return 'closed'








                  

