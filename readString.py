

# location = "Cedar Wood Park"
# locationChoppped = location.split(" ")
# print (locationChoppped[-1])

try:
   myfile=open('oalaa.txt')

   for i in myfile:
      print(i,end='')

except IOError as err:
    print('Please fix the nme of file: {}'.format(err))