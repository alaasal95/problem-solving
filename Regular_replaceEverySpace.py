
import re

txt='Alaa Salim Hussain Ate'

x=re.sub('\s','_',txt)
print(x)
print('****************')
#replce the first two Space

x=re.sub('\s','[]',txt,2)
print(x)
