


words="alaa salim"
index=0
counter=0
print('the lenght of words=',len(words))
print(len(words[-1]))
for num,index in enumerate(words):



     if (index == ' '):
       counter=counter+1
       continue
     elif(index ==len(words[-1])):
       counter=counter+1
     print('number {} for ={}'.format(num, index))
print('Counter=',counter)




















# address = input("Enter IP = ")
# i=0
# while (i<len(address)):
#
#   for index in address:
#
#     if(index == .):
#     print(address[i],end='')
#     i=i+1