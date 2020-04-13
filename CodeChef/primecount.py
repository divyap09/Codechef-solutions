import math
a=2
sum=2
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
                if(comp<1):
                                sum=sum+a
                                print(a)
                                
                if(a>=2000000):
                                print(sum)
                                break
