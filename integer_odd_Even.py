

'''
      ----->Ex://  read number and check if it's integer(odd or even) or not integer
'''

#
# running=True
# while(running==True):
#
#      key=input('Enter { open }for open the program Or { close }for Close the program=')
#
#      if(key=='close'):
#          print('Done...')
#          running=False
#      elif(key=='open'):
#          num=int(input('Enter Number='))
#          if(num%2==0):
#              print(num,'is Even')
#          else:
#
#              print(num,'is Odd')
#
#


def main():
    Alaa()

def Alaa():


    Even_Odd()

def Even_Odd():
    running = True
    while (running == True):



     key=input('Enter { open }for open the program Or { close }for Close the program=')

     if(key=='close'):
         print('Done...')
         running=False
     elif(key=='open'):
         num=int(input('Enter Number='))
         if(num%2==0):
             print(num,'is Even')
         else:

             print(num,'is Odd')


if __name__ == '__main__':main()
