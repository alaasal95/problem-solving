
def main():
    num1=int(input('Enter 1st number{x}='))
    num2= int(input('Enter 2st number{y}='))
    maxnum(num1,num2)



def maxnum(x,y):

  if(x>y):
      print('the largest number x=',x)
  elif(y>x):
      print('the largest number y=', y)
  elif(x==y):
      print('x=',x ,'is equal to','y=' ,y, )


if __name__ == '__main__':main()
