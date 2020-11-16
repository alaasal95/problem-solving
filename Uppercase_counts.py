


'''
 ----->Ex:// using function to counts uppercase letter in
             20 letters entered by the user in the main program.
'''




def main():
    Alaa()


def Alaa():
        n=input('enter letter=')
        uppercase(n)
        lowercase(n)




def uppercase(n):

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']

    for i in uppercase:

        if (n == i):
            print('the letter', i, 'uppercase')


def lowercase(n):
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
    for j in lowercase:

        if (n == j):
            print('the letter', j, 'lowercase')



if __name__ == '__main__':main()
