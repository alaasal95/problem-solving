







class car():
    def __init__(self,**kwargs):
        self.Data=kwargs


    def Get_CarOnwer(self):
        print('Owner name:'+self.Data['Name'])

        print('Model car:'+self.Data['Model'])



def main():


    BmCar=car(Name='alaa salim',Model='BMW 2008')

    BmCar.Get_CarOnwer()

    # oudiCar=car('mark zak','OUDI')
    # oudiCar.Get_CarOnwer()



if __name__ == '__main__':main()


