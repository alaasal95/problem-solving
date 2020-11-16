
# ∑_(i=1)^n▒〖i^2=1^2+2^2+3^2 〗+⋯+n^2

i=1
sum=0
n=int(input('Enter n='))

while (i<=n):

     sum=sum+(i*i)
     print('summ in=',sum)
     i=i+1

print('The summation=',sum)