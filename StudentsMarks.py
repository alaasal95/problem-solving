


m=[None]*3

i=0
while(i<3):
    n=int(input('enter num='))
    m[i]=n

    i=i+1


print(m,type(m))


while(i<3):

    if(m[i] <50 or m[i]>100):
        print()