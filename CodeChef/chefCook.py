m=int(input())
li=[]
while m>0 :
                m=m-1
                li=input()
                ch,co,k =li.split()
                ch=int(ch)
                co=int(co)
                k=int(k)

                #ch=int(input())
                #co=int(input())
                #k=int(input())
                sum=ch+co
                sum=sum%(k*2)
                if sum <=(k/2) :
                                print("CHEF")
                else:
                                print("COOK")
