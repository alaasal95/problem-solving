







class car():
    def __init__(self,name,carType):
        self._name=name
        self._carType=carType


    def Get_CarOnwer(self):
        print('name onwer - {} - of car:{}'.format(self._name,self._carType))

    def setName(self,namee):
            self._name=namee

    def getName(self):
        return self._name
def main():


    BmCar=car('alaa salim','BMW')

    BmCar.Get_CarOnwer()

    oudiCar=car('mark zak','OUDI')
    oudiCar.Get_CarOnwer()

    kk=car('zahraa','TASLA')
    kk.setName('facebook')
    print(kk.getName())




if __name__ == '__main__':main()


