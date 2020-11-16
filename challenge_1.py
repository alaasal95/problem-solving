

'''

------>EX:// Introduce a function called Count Words, when you call it we pass a text to it,
             and it returns the number of words in that text.Then try this function in the program.

Example: If she uses a role in CountWords () in the text "Easy-to-Learn Programming."
         Apple will return the number 5.

'''



#t1='Programming is easy to learn.'

def CountWords(t1):

        length=len(t1)
        print('length:',length)
        print('==================================')
        i=0
        counter=0
        x=-1
        while(i<len(t1)):
           # print('i:',i,'====>>>',t1[i])
            if(t1[i]==' '):
               # print('t1-->',t1[i])
                counter=counter+1

            elif(i==length-1):
              #  print(t1[i],'t1=***>',t1[-1])
                counter=counter+1
            i=i+1

        print('counter:',counter)



tex=input('enter your text:')
sed_all=CountWords(tex)


#######################################################

#
# last=t1[length-1]
# i=0
# while(i<len(t1)):
#     if(i==length-1):
#         print(i,'=',last)
#
#
#     i=i+1

#######################################################