#edit code luyentoan
import random
import time
cacdau=("+","-","x",":")
while 1:
	dung=0
	sai=0
	i=1
	tl=0
	print'Chuong trinh luyen toan - mathtest.v1 by TuanMerino'
	print'let\'s go'
	socau=int(input('So cau: '))
	for i in xrange(1,socau+1):
		if 1:
			dau=random.choice(cacdau)
		if (dau=="x"):
			a=random.randint(10,100)
			b=random.randint(1,10)
			kq=a*b	

			print 'cau '+str(i)+ ': '+str(a)+' '+str(dau)+' '+str(b)+' ='
			time.sleep(5)
			tl=raw_input('')
		if (dau==":"):
			if 1:
				a=random.randint(10,1000)
				b=random.randint(1,10)
				if a%b==0:

					print 'cau '+str(i)+ ': '+str(a)+' '+str(dau)+' '+str(b)+' ='
					time.sleep(5)
					tl=raw_input('')
			else:
				continue
			kq=a/b
		if (dau=="+"):
			a=random.randint(100,10000)
			b=random.randint(100,10000)		
			kq=a+b

			print 'cau '+str(i)+ ': '+str(a)+' '+str(dau)+' '+str(b)+' ='
			time.sleep(5)
			tl=raw_input('')
		if (dau=="-"):
			if 1:
				a=random.randint(100,10000)
				b=random.randint(100,10000)
				if (a>=b):

					print 'cau '+str(i)+ ': '+str(a)+' '+str(dau)+' '+str(b)+' ='
					time.sleep(5)
					tl=raw_input('')
				else:
					continue
			kq=a-b
		if tl==str(kq):
			print'dung'
			dung=dung+1
		else:
			print'sai hoac khong hop le'
			sai=sai+1
			

		f = open('luyentoan.txt', 'a')
		f.write('\n'+'cau '+str(i)+ ': '+str(a)+' '+str(dau)+' '+str(b)+' =' +str(tl)+' dap an '+str(kq))
		f.close()

	f = open('luyentoan.txt', 'a')
	f.write('\n'+'so cau tra loi '+str(i)+' cau, dung: '+str(dung)+' ,sai :'+str(sai) )
	f.close()
	print 'dung: '+str(dung) +' sai: '+str(sai)
	time.sleep(4)
		
