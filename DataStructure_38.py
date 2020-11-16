


op={'orange','cherrey','eggeplant','apple','pear'}
op2={'orange','cherrey','eggeplant','apple'}

#المجموعةissupersetالشاملة:-الثاني هو مجموعة شاملة على الاول
pool=op2.issuperset(op)
print(pool)
#المجموعةissubsetالفرعية:-الثاني هو جزء من الاول
pool2=op2.issubset(op)
print('subset=',pool2)

#عملية اتحاد مجموعتين

un=op.union(op2)
print(un)
print('****************')
un2=op2.union(op)
print(un2)

inter=op.intersection(op2)
print(inter)
op.pop()
print(op)
#يمسح عنصر عنصر
op.pop()
print(op)