import ftplib
from ftplib import FTP

print("FTP Anon Login Checker By ShikataGaNai")
address = input("Enter Host IP/Domain:")

print("Trying Anonymous Login To: " +address)

user ='anonymous'
pas ='anonymous'


ftp = FTP(address)
ftp.login(user,pas)

ftp.dir()

