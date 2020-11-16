

'''
----->Ex:// using function,to inputs a student's avarage and
            return 4 if student's average is 90-100,3 if the average is 80-89
            2 if the average is 70-79,1 if the average is 60-69,and 0 if the average is lower
            than 60
'''




#
#
# num=float(input('Enter Your average='))
#
# if(num>=90 and num<=100):
#     print('yor GBA=4')
#
# elif(num>=80 and num<=89):
#     print('yor GBA=3')
# elif (num >= 70 and num <= 79):
#     print('yor GBA=2')
# elif (num >= 60 and num <= 69):
#     print('yor GBA=1')
# elif (num < 60):
#     print('yor GBA=0')
#
#
#
#
#



def main():
    Alaa()

def Alaa():
    num = float(input('Enter Your average='))

    if (num >= 90 and num <= 100):
        print('yor GBA=4')

    elif(num>=80 and num<=89):
        print('yor GBA=3')
    elif (num >= 70 and num <= 79):
        print('yor GBA=2')
    elif (num >= 60 and num <= 69):
        print('yor GBA=1')
    elif (num < 60):
        print('yor GBA=0')


if __name__ == '__main__':main()
