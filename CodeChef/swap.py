n=int(input())
result=0
while n>0 :
                three=input()
                m,x,s=three.split()
                m=int(m)
                x=int(x)
                s=int(s)
                result=int(x)
                while s >0 :
                                two=input()
                                a,b=two.split()
                                a=int(a)
                                b=int(b)
                                a,b= (b,a)
                                if(a== result) :
                                                result=b

                                else :
                                                result=a
                                s=s-1
                n=n-1
print (result)
                                
