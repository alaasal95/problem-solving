










a=['a','b','c','#','d','e','f','#','h','i','j']

print(a)
print(len(a))
print('after=',len(a))

print('***************************')
print()
print()
i=0
j=1
while(i<len(a)-1):
  if(a[i]!='#' and a[j]!='#'):
            a[i]=a[i]+a[j]
            print('deleted=', a.pop(j), '(', j, ')')
            print(i, '=', a[i])

            print('a=',a)
            #j = j + 1
           # print('j=',a[j],'======>>>', j)
            print()
            print()
          #else:print('----------->',j)


  elif(a[j]=='#'):
      print('Del@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=', a.pop(j), '(', j, ')')
      i=i+1   #i=1 #i=2
      j=i+1   #j=2 #j=3

print('--------------------------------------------------------------')
print('--------------------------------------------------------------')
print('a_Total=',a)
print('--------------------------------------------------------------')
print('--------------------------------------------------------------')

name='def'
k=0
while(k<len(a)):
     if(name==a[k]):
         print(a[k])
     k=k+1



#
# aa=['a','b','c','d']
# i=0
# j=0+1
# while(i<len(aa)):
#     if(aa[i]!=' '):
#
#         aa[j]=aa[i]+aa[j]
#         aa.pop(i)
#         print('aa=',aa)
#
#     else:
#
#         print(i, '=', '#')
#
#     i = i + 1
#
# print(aa)
#





#
#
#
#
#
#
#
#
#
# aa=['a','b','c','','d','e','f','','g','h','i']
#
# #bb=['','','']
# # i=0
# # j=0
# # bb[0]=aa[0]+aa[0+1]
# #
# #
# print(aa)
# i=0
# j=0
# while(i<len(aa)):
#     if(aa[i+1]!=''):
#
#         aa[j]=aa[j]+aa[i]
#         print('bb_=',aa)
#     elif(aa[i]==''):
#         j=j+1
#         aa[j]=aa[i]
#         print('bb*=', aa)
#
#
#     i=i+1
#
# print('bb_Total=',aa)
#
#
#


