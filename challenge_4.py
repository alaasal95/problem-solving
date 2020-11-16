

'''

---->Ex://Enter two texts and it checks if the second text is in the first text or not
'''


def main():
    Alaa()

def Alaa():

        a=list(input('enter your string='))
        #print(type(a))
        #print(len(a),type(a))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~```')


        print('***************************')
        print()
        print()

        Repeted(a)
        name = input('enter your string=')
        Ocurrenc(a,name)

def Repeted(a):

        i=0
        j=1
        while(i<len(a)-1):
          if(a[i]!=' ' and a[j]!=' '):
                    a[i]=a[i]+a[j]
                    a.pop(j)
                    # print('deleted=', a.pop(j), '(', j, ')')
                    # print(i, '=', a[i])
                    #
                    # print('a=',a)
                    # j = j + 1
                    # print('j=',a[j],'======>>>', j)
                    # print()
                    # print()
                  #else:print('----------->',j)


          elif(a[j]==' '):
              a.pop(j)
            #  print('Del@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=', a.pop(j), '(', j, ')')
              i=i+1   #i=1 #i=2
              j=i+1   #j=2 #j=3

        print('--------------------------------------------------------------')
        print('--------------------------------------------------------------')
        print('a_Total=',a)
        print('--------------------------------------------------------------')
        print('--------------------------------------------------------------')






def Ocurrenc(a,name):
#name='hussain'

        counter = 0
        #print(len(name),type(name))
        k=0
        while(k<len(a)):
             if(name==a[k]):
                 print(a[k])
                 counter=counter+1

             k=k+1
        print('counter=',counter)




if __name__ == '__main__':Alaa()
























# aa=[]
# aa=['a','b','c','x','','d','e','f','','g','h','i']
# bb=['','','']
#
# # i=0
# # j=0
# # bb[0]=aa[0]+aa[0+1]
# #
# #
# print(aa)
# i=0
# j=0
# while(i<len(aa)):
#     if(aa[i]!=''):
#
#         bb[j]=bb[j]+aa[i]
#         print('bb=',bb)
#     elif(aa[i]==''):
#         j=j+1
#         bb[j]=aa[i]
#         print('bb=', bb)
#     i=i+1
#
# print('bb_Total=',bb)

#
#
#
#
#
# print(True and True)#---->T
#
# print(True and False)#----->F
# print(False and True)
# print(False and False)
#
#
# print('*******************')
#
#
# print(True or True)
#
# print(True or False)
# print(False or True)
# print(False or False)#---->F
#
#



#----->2
# a=['a','b','c','d']
# a[0]=a[0]+a[1]
# print(a)
# a.pop(1)
# print(a)
#
#
#
#



#------>1
# a=[]
# a=input('enter your string=')
# print(len(a))
# i=0
# while(i<len(a)):
#     if(a[i]==' '):
#         print(i, '=', '#')
#     else:
#
#         print(i, '=', a[i])
#
#     i = i + 1
#
#




#
# #a=['a','b','c','#','d','e','f','#','h','i','j']
# a=['a','l','a','a','#','s','a','l','i','m','#','h','u','s','s','a','i','n']
# print(a)
# print(len(a))
# print('after=',len(a))







# # s هنا قمنا بتعريف متغير نصي إسمه
# s = "Hello, my name is Mhamad. I'm a full my stack developer."
# # s في النص الموجود في المتغير 'a' هنا قمنا بطباعة كم مرة يوجد النص
# print(s.count('my'))


