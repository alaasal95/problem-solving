




class operation:

    def sum(self,n1,n2):
        sumResult=n1+n2
        print('sumResult:',sumResult)
    def sub(self,n1,n2):
        subResult=n1-n2
        print('subResult:',subResult)
class Good(operation):
    def mul(self,m1,m2):
        result=m1*m2
        print('Result:',result)

def main():
    oop=Good()
    oop.sub(2,4)
    oop.sum(2,4)
    oop.mul(3,5)




if __name__ == '__main__':main()
