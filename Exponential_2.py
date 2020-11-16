


#---->>> e=1+[x]^1+([x]^2/1!)+([x]^3/2!)+...+([x]^a/a!)


f=1
e=0
a=int(input('Enter last factorial='))
x=int(input('Enter x='))
aa=1
while(aa<=a):

     f=f*aa
     e=e+(pow(x,aa)/f)
     print('e_in=',e)
     aa=aa+1
print('e=',e)
