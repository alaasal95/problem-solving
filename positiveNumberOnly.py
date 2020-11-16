


###--->read 10 integer numbers and find the sum of positive number only ?

num1=[None]*4
print('num=',num1,type(num1),len(num1))

input('Enter 10 numbers----')


i=0
while i <num1.__len__():
    num = int(input('enter number='))
    num1[i]=num
    i=i+1
print(num1,num1.__len__())


sum=0
j=0
while(j<num1.__len__()):

    if(num1[j]%2==0):
        sum=sum+num1[j]
    j=j+1

print('Sum=',sum)


