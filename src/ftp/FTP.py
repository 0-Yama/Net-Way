from ftplib import FTP 
class FTPConnector:

    def init(self, host ,user , password):                              #Methode de construction
        self.host      = host
        self.user      = user
        self.password  = password
        self.connected = False

    def connect(self):                                                      #methode 
        print(f'ftp.connect({self.host} {self.user} {self.password})')
        self.connected = True
        self.ftp = FTP(self.host)
        self.ftp.login(user=self.user, passwd=self.password)

    def upload(self, name,  file):
        file = open(file, 'rb')
        self.ftp.storbinary (f'STOR {name}', file)
        file.close

    def download(self, name, path):
        fp = open(path, 'wb')
        self.ftp.retrbinary(f'RETR {name}', fp.write)
        fp.close()

    def list (self):
        self.ftp.retrlines('LIST')

    def delete(self,file):
        self.ftp.delete(file)

    def createDirectory(self,directory):
        self.ftp.mkd(directory)

    def removeDirectory(self,directory):
        self.ftp.rmd(directory)

test =FTPConnector("127.0.0.1","msanatine","P@ssword1234")     #test est un objet qui appel la classe
test.connect()
test.list()                                                    #test appel la methode
test.download("transferfile.txt",'.\test.txt')
test.upload("testUpload.txt",'.\upload.txt' )
test.delete("commande.txt")
test.createDirectory("dossier4")
test.removeDirectory("dossier3")