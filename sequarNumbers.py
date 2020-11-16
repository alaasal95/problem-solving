



#----->Ex:// program to calculate the squared value of a number
#           passed from main function.Use this function in a
#          program to calculate the sequares numbers from 1 to 10




####----->main program<------
def main():

  SequarFun()



####----->main Function<------
def SequarFun():
    x = 1
    while (x <= 10):

        print('sequare number=',SequarFun1(x))

        x = x + 1


####----->Sup Function<------
def SequarFun1(y):
    result=y*y
    return (result)

if __name__ == '__main__':main()

