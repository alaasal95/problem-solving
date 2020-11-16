#
#
# ----->Ex:// i=1(E)n (i)^2=(1)^2+(2)^2+(3)^2+...+(n)^2


#
# i,n,sum=1,4,0
#
#
# while(i<=n):
#     sum=sum+(i*i)
#     i=i+1
# print('Sum=',sum)

def main():
    Alaa()


def Alaa():
    sum=0

    n=int(input('Enter last number='))

    print('Sum=', Summation(n, sum))



def Summation(n,sum):
  i=1
  while(i<=n):
    sum=sum+(i*i)
    i=i+1

  return (sum)


if __name__ == '__main__':main()
