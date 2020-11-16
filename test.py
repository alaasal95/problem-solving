





a=[None]*3

i=0
sum=0
running=True
while(running==True):
        key = input('enter {open} to running & {close} to finsh =')
        if (key == 'close'):
            print('Done.')
            running = False
        elif (key == 'open'):

                while(i<len(a)):
                    num=int(input('Enteer number='))

                    if(num<50 or num>100):
                        print('fail')
                        print(num)
                        a[i]=num
                        running = False
                        break

                    elif (num >= 50 and num <= 100):
                       a[i] = num
                       sum = sum + a[i]
                    i=i+1

                print('a=',a)
                print('sum=', sum)












