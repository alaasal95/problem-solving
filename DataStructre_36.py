



myList=list(range(5))
myTuple=tuple(range(7))

print(type(myList),'myList=',myList)
print(type(myTuple),'myTuple=',myTuple)

print(3 in myList)
print(33 not in myList)
myList.insert(2,102)
print('myList_insert=',myList)

myList3=myList.append(102)
print('myList_append=',myList3)

co=myTuple.count(2)
print('myTuple_count=',co)

isTuple=(1,2,3,1,7,5,1)
countit=isTuple.count(1)
print('countit=',countit)
indexes=isTuple.index(5)
print('indexes=',indexes)
