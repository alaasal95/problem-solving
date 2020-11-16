

'''

---->Ex://I write a program that asks the user to enter a number. Then it is shown to him whether this number is
          a Palindrome or not.
          Palindrome is a number whose numbers are evenly reversed from right to left and from left to right.

         Examples: The following numbers are all considered Palindrome numbers: 1001 - 123321 - 4554 - 45654.
'''



#a = '124521'
#a = '45654'
#a ='1245421'
#a ='12456421'
#a ='1234321'
a ='1234'
print(a)
for j,i in enumerate(a):
    print('j index {} for ={}'.format(j,i))

print('***************')
i = 0
j=-1
dd=len(a)/2
print('length total=',type(len(a)),len(a))
print('length/2=',type(dd),dd)
nag=-dd
print('nag=',type(nag),nag)
# Hr2=True
# Hr=True
print('*************************')
while i <dd and j>=(nag):
    # if i==dd:
    #     print('i====>',i)
    print('i==>',i)
    print('j==>',j)
    print(' ')
    if ( ( a[i] == a[j])):
         print('{',a[i],'}','is equal to =','{',a[j],'}')
        # print('Yes palindrom')


    elif( ( a[i] != a[j])):
        print('{',a[i],'}', 'is Not equal to =','{', a[j],'}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("-----------Result-----------")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('===>{ Done.. This Number not palindrom Number }<===')

    i = i + 1
    j = j - 1


# if Hr:
#     print('No..this number {Not Palindrome } Number')
# elif Hr2:
#    print('Yes..this number { Palindrome } Number')
