
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
for i in x:

    if i==x[-1]:

        print('the length of ','{',i,'}','=',len(i))
