a=0
b=1
c=a+b
count=0
while(a<4000000) :
                c=a+b
                if(a%2==0) :
                                count=count+a
                a=b
                b=c
print(count)
