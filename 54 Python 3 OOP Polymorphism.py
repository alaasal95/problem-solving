
'''
ملاحظة-مهمه://حتى يتحقق البولمورفزم يجيب ان يتحقق شرطين:-
1-يجب ان تتحقق الوراثة
2-يجب ان تتحقق الوفرايد

'''


class Shape():

    def printVal(self):

           print('Shape')

class Circle(Shape):
    def printVal(self):

           print('Circle')

class Rectangle(Shape):
    def printVal(self):

           print('Rectangle')



class A:
    def draw(self,a:Shape):
        a.printVal()


def main():

    x=Shape()
   # x.printVal()
    obj=A()
    obj.draw(x)
    obj.draw(Circle())
    obj.draw(Rectangle())

    # y=Circle()
    # y.printVal()
    #
    # z=Rectangle()
    # z.printVal()


if __name__ == '__main__':main()


