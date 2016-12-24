#!/usr/bin/python           
import max7219.led as led
import socket    ,os          
s = socket.socket()         
host = socket.gethostname() 
port = 1234            
s.bind((host, port))        

s.listen(500)  
def main(data):
    try:
	device = led.matrix(4)
	device.orientation(90)
	device.brightness(10)
	device.show_message(data)
	
def run():
	try:
		while True:

			c, addr = s.accept()
			data=c.recv(10294)
			print 'Connection from', addr
			print data
			main(data)
#			c.send('Thank you for connecting')
#			os.system(data)
			c.close()       
	except:
		run()
run()
