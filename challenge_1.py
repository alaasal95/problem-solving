

'''
---->Ex://I write a program that asks the user to enter a number.
         Then he displays the result of adding the numbers of this number.
         Example: If the user enters the number 123, the sum of his numbers
         will be calculated as 1 + 2 + 3, and the result will be 6 .

'''


s = 0
n = int(input('Enter a number: '))

while n != 0:
    s += n % 10
    print('the s=', s )
    n = int(n / 10)
    print('The n=',n)

print('The sum of the digits is: ' + str(s))
