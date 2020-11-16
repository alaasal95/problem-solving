

'''
----->Ex:// using function,to inputs a student's avarage and
            return 4 if student's average is 90-100,3 if the average is 80-89
            2 if the average is 70-79,1 if the average is 60-69,and 0 if the average is lower
            than 60
'''






num=[None]*8


def main():
    Alaa()

def Alaa():

    Aver()



def Aver():
    i = 0
    sum=0

    running=True
    while(running==True):
        key=input('enter {open} to running & {close} to finsh =')
        if(key=='close'):
            print('Done.')
            running=False
        elif(key=='open'):
                    while (i < len(num)):
                        num[i] = int(input('Enter Number='))


                        Check = Check_it(num[i])
                        i = i + 1

                    print(num)

########################################################################################################################

                    if (Check == 'fail'):
                         print('<<---you are fail best wishes for you in the next year--->>')

                    elif(Check=='pass'):

                        print('you are paas ')
                        sum = sum + num[i]

                        print('Summation=', sum)
                        # length = len(num)
                        #
                        # average = sum / length
                        #
                        # print('average=', average)
                        # print('the number for average=', Aver_det(average))



########################################################################################################################



def Check_it(num):
    print('list_num',num)

    j=0
    while(j<num):
        if(num[j]>=50 and num[j]<=100):
            ru='pass'
            print(j,'====>',num[j])
            return (num[j])

        elif(num[j]<50 or num[j]>100):
            ru='fail'
            print(j, '====>', num[j])
            return (ru)

        j=j+1





########################################################################################################################
# def Aver_det(av):
#
#     if(av>=90 and av <=100):
#         printting=4
#         return printting
#     elif(av>=80 and av<=89):
#         printting = 3
#         return printting
#     elif (av >= 70 and av <= 79):
#         printting = 2
#         return printting
#     elif (av >= 60 and av <= 69):
#         printting = 1
#         return printting
#     elif (av > 60):
#         printting = 0
#         return printting
#



if __name__ == '__main__':main()
