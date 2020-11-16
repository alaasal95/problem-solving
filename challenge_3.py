

'''

---->EX// Define a function We pass a text to her when she is summoned, and she returns to us a copy of this text,
           each letter in which is repeated twice.

'''



def DoubleChars(s):



        print('length_s:',len(s))


        x=''
        i=0
        while(i<len(s)):


            x=x+s[i]+s[i]
            i=i+1
        return (x)



text=input('enter text:')

doubletwice=DoubleChars(text)

print('the double charchter:'+doubletwice)



