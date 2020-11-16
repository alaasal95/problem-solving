

class car():
    def __init__(self,name,carType):
        self._name=name
        self._carType=carType


    def Get_CarOnwer(self):
        print('name onwer - {} - of car:{}'.format(self._name,self._carType))



def main():


    BmCar=car('alaa salim','BMW')

    BmCar.Get_CarOnwer()

    oudiCar=car('mark zak','OUDI')
    oudiCar.Get_CarOnwer()



if __name__ == '__main__':main()




# class animal:
#     def __init__(self):
#         print('python programmer')
#     def souund(self):
#         print('this is animal sound')
#
#     def runAnimal(self):
#         print('animal is runing')
#
#
# dog=animal()
# #cat=animal()
# #
# # dog.souund()
# # cat.runAnimal()
# #
# # print(type(dog))