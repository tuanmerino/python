#program by Tuanmerino
#coding: utf-8
import math
def hpt(a1,b1,c1,a2,b2,c2):
    d=a1*b2 - a2*b1
    dx=c1*b2 - c2*b1
    dy=a1*c2 - a2*c1
    if d<>0 : 
	    x=dx/d
	    y=dy/d
	    print ('he phuong trinh co nghiem x=%s y=%s') %(x,y)
    else:
        if dx==0 and dy==0 :
            print 'he phuong trinh vo so nghiem'
        if dx==0 or dy==0:            
            print 'he phuong trinh vo nghiem'	
print"""
         He phuong trinh bac nhat co dang        
		 +- a1x + b1y = c1
	    <=
		 +- a2x + b2y = c2
                                            """		  
a1 = float(input('he so a1: '))
b1 = float(input('he so b1: '))
c1 = float(input('he so c1: '))
a2 = float(input('he so a2: '))
b2 = float(input('he so b2: '))
c2 = float(input('he so c2: '))
print' Phuong trinh cua ban la '
print('%sx+%sy=%s') %(a1,b1,c1)
print('%sx+%sy=%s') %(a2,b2,c2)
hpt(a1,b1,c1,a2,b2,c2)
