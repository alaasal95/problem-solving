


#------>Sum=1+1/1!+2/2!+3/3!+....+n/n!


i=1
n=3
sum=0
f=1
while(i<=n):
    f=f*i
    sum=sum+(i/f)
    print('Sum_in=',sum)
    i=i+1


print('Sum_Total=',sum)