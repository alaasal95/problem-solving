
#
# ###
#
# ********
#  ********
# ********
#  ********
# ********
#  ********
# ********
#  ********
# ###



# i=1
#
# while (i<=8):
#
#      if (i%2==0):
#          print(i,'=','$********')
#          i=i+1
#      elif (i%2==1):
#          print(i,'=','********$')
#          i=i+1
#
#


####---Second way to solve this problem----
row = 8

while (row > 0):

    col = 8
    if (row % 2 == 0):
        print('$',end='')
    while (col > 0):
        print('*',end='')
        col=col-1
    print()
    row=row-1