#!/data/data/com.termux/files/usr/bin/python3
# sengaja up ke github ,biar gak ilang 
# udah 2x ke delete ,
# kusonime url parse / males lewat shortlink 
from urllib.parse import unquote

def geturl():
	url = input('[*] url ? : ')
	parze = unquote(url.split('url=')[-1].split('&')[0])
	print('[*] result !')
	print(f'\n{parze}\n')
	geturl()

if __name__=="__main__":
	geturl()

# https://semawur.com/full/?api=3f184c48f4342c9bfd30a87a3f14dc9b57934868&url=https%3A%2F%2Fdrive.google.com%2Fuc%3Fexport%3Ddownload%26id%3D1Riv56Pd5t6tnm_wNhwMNAwUe3OFITQNI&type=2
