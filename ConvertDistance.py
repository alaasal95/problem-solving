

def main():
    Alaa()


def Alaa():

    feet_to_meter()
    inch_to_meter()



def feet_to_meter():

        feet=int(input('enter feet number='))

        convert_to_meter=feet*0.3048

        print('from feet to meter=',convert_to_meter)


def inch_to_meter():

     inch=int(input('enter inches number='))
     convert_to_inches=inch/39.370
     print('from feet to inches=', convert_to_inches)


if __name__ == '__main__':main()
