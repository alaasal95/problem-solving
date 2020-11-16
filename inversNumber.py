
size_list=int(input('Enter size list='))

a=[None]*size_list
print(type(a))
k=0
while(k<len(a)):
    number = int(input('Enter number of list='))
    a[k]=number
    k=k+1
print('list {a}=',a)
b=[None]*size_list

i=0
j=-1

while(i<len(b)):

    b[i] = a[j]
    j=j-1
    i= i + 1

print('b=', b)
