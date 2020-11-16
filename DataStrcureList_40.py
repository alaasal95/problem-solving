
list=[1,2,3,5,6,7,9]
li=list[2:10:2]
print(list)
print(li)
list[2:10]=(144,144,144,144,50,60)
print(list)

print(range(1,16))

for i in range(1,16):
    print(i)

list[:]=range(0,20,2)
print(list)
list[:]=range(40)
print(list)