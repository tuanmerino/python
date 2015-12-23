#program by tuanmerino
print """ 	Chuong trinh tim so cac so chia het cho n trong day tu a den b 
																		                                        	"""
a=int(raw_input('Nhap a: '))
b=int(raw_input('Nhap b: '))
n=int(raw_input('nhap n: '))
def abc(a,b,n):
	d=0
	for m in range(a,b+1) :
		if m%n==0:
			d=d+1
			print" cac so chia het cho %s la %s" %(n,m)
	print" so cac so chia het cho %s la %s" %(n,d)
	return 
abc(a,b,n)			
