

'''
---->Ex://Then after the next stage, it asks you to wait for the resulting text and store it
          in three text variables: S1, S2, and S3.
          1. It tells him whether or not merging S1 with S2 equals S3.
          2. It tells him if S1 is a part of S2 or equal to (i.e. S1 == s2).
          3.If the length of S1 is greater than the length of S2, then text S2
            text over S1 and store a new text variable named S4.
          4.If the length of S2 is greater than the length of S1 then add the
            text S1 on S2 and store the result in a new text variable named S4.
          5.It tells him if S2 is a fraction of the second half of S1.
          6.It shows the characters in the first half of S1.

'''




s1='alaa'
s2='salim hussain'
s3='alaa salim hussain'


print('s1:',s1)
print('s2:',s2)
print('s3:',s3)

print('----------------------')
#====>1
if(s1+' '+s2==s3):
    print('Yes it is equal...')
else:
    print('No it is not equal')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#====>2
if(s1==s2):
    print('Yes ( {} ) Similar to ( {} ) ...'.format(s1,s2))
else:
    print('No ( {} ) is not Similar to ( {} )...'.format(s1, s2))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#====>3
s1_length=len(s1)
s2_length=len(s2)
s4=''
print('s1_length:',s1_length,'  ,  ','s2_length:',s2_length)

if(s1_length>s2_length):
    s4=s2+' '+s1
    print('the "{s1_length > s2_length}"==>s4:',s4)
elif(s2_length>s1_length):
    s4=s1+' '+s2
    print('the "{s2_length > s1_length}"==>s4:',s4)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#====>4
ss1='zahraa saad'

ss2='ad'
print('ss1:',ss1)
print('ss2:',ss2)
ss2_length=len(ss2)
j=0
while(j<len(ss1)):

    if(ss1[j:j+ss2_length]==ss2):
        print(ss1[j:j+ss2_length])
    j=j+1

k=0
while(k<len(ss1)):

    if(ss1[k]!=' '):
            print(ss1[k],',',end='')
    else:
        break
    k=k+1
