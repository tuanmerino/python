import mmap
import os
import glob


d=0
while 1:
	d=0
	tf=raw_input('Dang tap tin: ')
	a= glob.glob("*."+tf+"")
	data=raw_input('Du lieu tim kiem: ')

	for i in xrange(len(a)):
		randomfile=a[i]
		f = open(randomfile)
		s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
		if s.find(data) != -1:
			d=d+1
			print 'Da tim kiem thay du lieu '+ '('+data+')'' trong '+str(randomfile)
			
		else:
			print 'Khong tim thay du lieu '+'('+data+')'+' trong '+str(randomfile)
	print str(a)+'Tim thay '+str(d)+' ket qua'		
