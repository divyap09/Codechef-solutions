n=int(input())
while n>0 :
                m=int(input())
                i=int(1)
                fact=int(1)
                while i<=m :
                                fact=fact*i
                                i=i+1
                count=0
                stri=str(fact)
                le=len(stri)
                while le>0:
                                if stri[le-1]=='0':
                                                count=count+1
                                else :
                                                break
                                le=le-1
                print(count)
                n=n-1
                                
