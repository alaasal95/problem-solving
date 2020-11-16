
s=1
i=1
runing=True

while(runing==True):
  key=int(input('enter (1) for Open the program (0) for Close the program='))
  if(key==0):
      print('Finsh')
      runing = False
  elif(key==1):
        m = int(input('Enter m='))
        n = int(input('Enter n='))
        while(i<=m):


           s=s*n
           i=i+1


        print('s=',s)
        print('Done..')

