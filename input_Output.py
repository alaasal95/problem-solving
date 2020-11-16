
f1=open('alaa.txt')
f2=open('alaa_w.txt','a')
lis=[1,2,2,4,3]

for i in lis:
    print(i,file=f2,end='')
