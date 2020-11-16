

#---->>> e=1+(1/1!)+(1/2!)+(1/3!)...+(1/n!)

nn=1
f=1
e=0
n=int(input('Enter last factorial number number='))

while(nn<=n):

     f=f*nn
     e=e+(1/f)
     nn=nn+1
print('e=',e)

e=e+1
print('exp=',e)
