


mydict={1:'alaa',2:'salim',3:'hussain',4:'atee'}

print(mydict)
mydict2=dict(a='alaa',s='salim',h='hussain')
print(mydict2)
print('s' in mydict2)

for x in mydict:
    print(x)

for x,n in mydict.items():
    print(x,n)

print(mydict.get(5,'not exitst'))

del mydict2['h']
print(mydict2)
#sets===> تستخدم للاشياء غير المكررة
mySets={'UOT','UOB','UOK'}
print(mySets)

a=set('asakdsala')
print(a)
a={x for x in 'asakdsala' if x not in 'abc'}
print(a)