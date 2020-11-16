

#----> Sum=1+(2)^2+(4)^2+...+(n)^2



sum=0
num=2
n=int(input('Enter n='))
while(num<=n):
    sum=sum+pow(num,2)
    num=num+2
print('sum=',sum)
