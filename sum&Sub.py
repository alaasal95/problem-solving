

#----> Sum=(1)^x-(3)^x+(5)^x-...+(n)^x

i=1
sum=0
n=int(input('Enter last number {n}='))
x=int(input('Enter Upper number{x}='))

while(i<=n):

    if(sum>0):
        sum=sum-pow(i,x)
        print('sum-i=',sum)
    elif(sum<=0):
        sum=sum+pow(i,x)
        print('sum+i=',sum)
    i=i+2

print('Total sum=',sum)