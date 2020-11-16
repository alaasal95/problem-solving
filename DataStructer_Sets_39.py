


s1={'alaa','mustafaa','wareeth','abaas','haider'}
s2={'alaa','abaas','sadek'}

subset=s2.issubset(s1)
print('subset=',subset)

super=s1.issuperset(s2)
print('super',super)

union1=s1.union(s2)
print('union1=',union1)
interSec=s1.intersection(s2)
print('interSec=',interSec)
deleted=s1.remove('abaas')
print('deleted=',s1)
poped=s1.pop()
print('poped=',poped,s1)

differ=s1.difference(s2)
print('differ=',differ)
s2.add('hussain')
print('s2=',s2)
s1.update(s2)
print(s1)