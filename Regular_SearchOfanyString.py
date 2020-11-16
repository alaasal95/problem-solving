

import  re


txt='Alaa Salim Hussain Atee'


x=re.search('A',txt)
if x:
    print('Yes.find')
else:
    print('No')