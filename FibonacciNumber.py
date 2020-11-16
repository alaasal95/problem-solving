


'''
 ----->Ex://    the Fibonacci series is:0,1,1,2,3,5,8,13,21,...it begins with
                terms 0 and 1 and has the property that each succeeding term is the
                sum of the two preceding terms.using function to calculate the nth Fibonacci number
'''


#
# a=[None]*9
#
#
#
# a[0]=0
# a[1]=1
#
# print(len(a))
# print('****************************')
# j=2
# while(j<len(a)):
#
#      a[j]=a[j-1]+a[j-2]
#      print('j-',j,'=',a[j])
#      j=j+1
#
# print(a)
#
# #####################################################
# k=0
# sum=0
# while(k<len(a)):
#
#     sum=sum+a[k]
#
#     k=k+1
#
# print('sum_Total=',sum)
#
#

########################################################################################################################


########################################################################################################################




a=[None]*9

def main():
    Alaa()


def Alaa():

    top=cal(a)
    summation(top)




def cal(a):
    a[0] = 0
    a[1] = 1
    j = 2
    while (j < len(a)):
        a[j] = a[j - 1] + a[j - 2]
        print('j-', j, '=', a[j])
        j = j + 1
    print('a=', a)


def summation(top):
    k = 0
    sum = 0
    while (k < len(a)):
        sum = sum + a[k]

        k = k + 1

    print('sum_Total=', sum)



if __name__ == '__main__':main()

