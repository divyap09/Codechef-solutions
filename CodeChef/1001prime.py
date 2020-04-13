import math
a=2
count=1
while True :
                a=a+1
                i=2
                comp=0
                sq=int(math.sqrt(a))
                sq=sq+1
                while i<sq :
                                if(a%i==0):
                                  comp=comp+1
                                i=i+1
                if(comp==0):
                                count=count+1
                if(count==10001):
                                print(a)
                                break
