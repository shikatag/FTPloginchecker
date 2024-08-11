# FTPloginchecker
Hedef sunucuda çalışan FTP servisinin anonymous login izni verip vermediğini öğrenebileceğiniz bir tool.

Eğer anonymous login var ise program sunucuda "dir" komutunu çalıştırır. Böylece login olup olamadığınızı anlayabilirsiniz. Eğer hata verir ise anonymous login yok demektir.

YASAL UYARI: Program kullanılarak yapılan her şey kullanan kişinin sorumluluğundadır. Geliştirici hiç bir şekilde sorumluluk kabul etmez.

KULLANIM:

1 - git clone https://github.com/shikatag/FTPloginchecker.git
2 - cd FTPloginchecker
3 - pip install ftplib
4 - python ftp_checker.py
