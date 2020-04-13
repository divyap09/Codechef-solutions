n=int(100)
fact=int(1)
while n>0:
                fact=fact*n
                n=n-1

sum=int(0)
#print(fact)
while int(fact)>0:
                sum=sum+ fact%10
                fact=fact/10
print(sum)
