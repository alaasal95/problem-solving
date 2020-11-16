



numTupl=(1,2,3,4,5)
numList=[1,2,3,4,5,6]
print(type(numTupl),'Tuple=',numTupl)
print(type(numList),'List=',numList)
myList=list(range(10))
print(myList)

myTuple=tuple(range(10))
print(myTuple)


print('---------------------')


print('numTupl[2]=',numTupl[2])

print('numTupl[2]=',numList[2])

print('---------------------')



print('numTupl[-1]=',numTupl[-1])

print('numTupl[-1]=',numList[-1])

print('---------------------')

numList2=[1]
numTupl2=(1,)
print('numList2=',numList2,'====>',type(numList2))
print('numTupl2=',numTupl2,'====>',type(numTupl2))