


buffer=452

f1=open('alaa.txt','r')
f2_w=open('alaa3_w.txt','w')
buffer=f1.read(buffer)
while len(buffer):
    f2_w.write(buffer)
    buffer=f1.read(buffer)
print('Done...')