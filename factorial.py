


###-----> n!=n*n-1*n-2*n-3...*2*1



n=int(input('Enter n='))
f=1

while(n>0):
    f=f*n
    n=n-1
print('factorial =',f)