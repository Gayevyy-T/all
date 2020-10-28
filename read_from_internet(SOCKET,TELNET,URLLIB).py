import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) #--> open a socket to the site
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()#->preparing data to send request and encode(I have to send first).HTTP/1.0\r\n\r\n means enter+enter'
mysock.send(cmd)

while True:
    data = mysock.recv(512) #-> receive up to 51 characters
    if len(data) < 1:
        break
    print(data.decode()) #-> printing received data and decoding

mysock.close()
 #===============the_same==============================================
 import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())
    
#COUNT WORDS:
#counts = {}
#for line in fhand:
#    words = line.decode().split()
#    for word in words:
#        counts[word] = counts.get(word, 0) + 1
#print(counts)
    




