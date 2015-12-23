#coding:utf-8
#Program by Tuan Merino
import math
def pt(a,b,c):
    delta = b*b - 4*a*c
    if delta > 0 :
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print "phuong trinh bac 2 co hai nghiem phan biet"
        print "x1= %3.2f x2= %3.2f " %(x1,x2)
    elif delta ==0 :
       print "phuong trinh co nghiem kep x1=x2= %3.2f" %(-b/2*a)
    else :
       print "phuong trinh vo nghiem"  
print "Nhap lan luot he so a,b,c cua phuong trinh bac 2"	   
a = float(raw_input('he so a:'))
b = float(input('he so b:'))
c = float(input('he so c:'))
pt(a,b,c)	   
	  
	  
