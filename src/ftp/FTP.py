print (__file__)
from ftplib import FTP 

ftp = FTP('127.0.0.1')
ftp.login(user='msanatine', passwd='P@ssword1234')
ftp.retrlines('LIST')
#ftp.cwd('/specificdomain-orlocation/')
fp = open('.\\transferfile.txt', 'wb')
print ("bonjour")
ftp.retrbinary('RETR transferfile.txt', fp.write)
fp.close()
file = open('./aaaa.txt', 'rb')
ftp.storbinary ('STOR aaaa.txt', file)
file.close
