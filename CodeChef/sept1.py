m=int(input())
while m>0 :
                result=int(0)
                list1= input()
                n,x,s= list1.split()
                n=int(n)
                x=int(x)
                s=int(s)
                temp=int(result)
                while s >0 :
                                t=input()
                                a,b=t.split()
                                a=int(a)
                                b=int(b)
                                if result==a :
                                                result=b
                                else :
                                                result=a
                                s=s-1
                print(result)

                m=m-1
