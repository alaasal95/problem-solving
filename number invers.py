#
#


t='     alaa salim'
print( t.capitalize())
print(t.upper())
print(t.center(45))
#يقوم بالغاء المسافات
print(t.strip())
print(t.replace('alaa','star'))
#يعكس الكبتل الى سمول والسمول الى كبتل
print(t.swapcase())
#to check if it can make it printing or nor
print(t.isprintable())
print(t.isdecimal())

t1='alaasalim'
print(t1.isalpha())
#to check if all it number or not
print(t.isalnum())
print(t.find('salim'))
#using to deleted the space form the last words or numbers
print(t.rstrip())
