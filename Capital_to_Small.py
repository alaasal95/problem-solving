


'''

   ----->Ex:/  using function ,to convert any Char. from cabital
               to small or from small to capital
'''

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']


def main():

    Alaa()


def Alaa():
        n=input('enter letter=')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        uppercase1(n,uppercase,lowercase)
        lowercase2(n,uppercase,lowercase)




def   uppercase1(n,uppercase,lowercase):
   # uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    #lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    i=0
    while(i<len(uppercase)):
        if(n==uppercase[i]):
            Top=i
            print('capeltal letter=',uppercase[i])
            j = 0
            while (j < len(lowercase)):
                # print(lowercase[j])
                if (Top == j):
                    print('small letter=', lowercase[j])
                j = j + 1
        i=i+1




######################################################################################################################


######################################################################################################################


def  lowercase2(n,uppercase,lowercase):
    #uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    #lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    k= 0
    while (k < len(lowercase)):
        if (n == lowercase[k]):
            Top2 = k
            print('small letter=', lowercase[k])
            l = 0
            while (l < len(uppercase)):
                # print(lowercase[j])
                if (Top2 == l):
                    print('capital letter=', uppercase[l])
                l = l + 1
        k = k + 1













    # for j in lowercase:
    #
    #     if (n == j):
    #         print('the letter', j, 'lowercase')
    #






if __name__ == '__main__':main()
