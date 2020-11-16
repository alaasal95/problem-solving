



'''
     ----->Ex://   write a function to find the largest int amaong three
                   int entered by the user in the main function
'''


#
# num1=int(input('enter 1st number='))
# num2=int(input('enter 2nd number='))
# num3=int(input('enter 3rd number='))
#
# if (num1>num2 and num1 >num3):
#     print('the largest number is num1',num1)
# elif(num2 > num1 and num2 > num3):
#
#     print('the largest number is num2',num2)
#
# elif (num3 > num1 and num3 > num2):
#
#     print('the largest number is num3', num3)
#


def main():

   Alaa()


def Alaa():
     num1 = int(input('enter 1st number='))
     num2=int(input('enter 2nd number='))
     num3=int(input('enter 3rd number='))


     print('the largest number is num1=', lagest(num1,num2,num3))



def lagest(x,y,z):

    if (x > y and x > z):
        return(x)

    elif (y > x and y > z):

        return (y)


    elif (z > x and z > y):


        return(z)



if __name__ == '__main__':main()