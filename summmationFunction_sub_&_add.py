


def main():
    Alaa()


def Alaa():

    n=int(input('enter n ='))
    x=int(input('enter x='))

    i=3
    sum=x
    sign=1
    while (i<=n):

        factorial=fact(i)
        pow1=power(x,i)
        sign=-1*sign
        temp=sign*(pow1/factorial)
        sum=sum+temp
        i=i+2
    print('Sum=',sum)



def fact(i):
    j=1
    f=1
    while(j<=i):

       f=f*j
       j=j+1
    return(f)


def power(x,i):

    result=pow(x,i)

    return (result)



if __name__ == '__main__':main()