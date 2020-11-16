






#
#challenge_1
# def reverse_string(s):
#
#     new_s = ''
#
#     for i in range(0, len(s)):
#         new_s = s[i] + new_s
#         print(i,'====>',s[i])
#
#     return new_s
#
#
# text = input('Enter any text: ')
#
# reversed_text = reverse_string(text)
#
# print('Reversed Text: ' + reversed_text)

#



#challenge_2
# number = int(input('Enter a number: '))
#
# reversedNumber = 0
# originalNumber = number
#
# while number != 0:
#     remainder = number % 10
#     reversedNumber = reversedNumber * 10 + remainder
#     number = int(number / 10)
#
# print('Reversed version of ' + str(originalNumber) + ' is: ' + str(reversedNumber))
#
#
#
#
#
#







#
#
##challenge_3
# def count_occurrences(s1, s2):
#
#     counter = 0
#
#     for i in range(0, len(s1) ):
#         if s1[ i:i + len(s2)] == s2:
#             counter += 1
#
#     return counter
#
#
# text = input('Enter any text: ')
# keyword = input('Enter word to search occurrences: ')
#
# result = count_occurrences(text, keyword)
#
# print("Total occurrences of '" + keyword + "' is: " + str(result))
#
# print('s=',len(text))
#
# print('s2=',len(keyword))
#



#
#
# def remove_all(s1, s2,s3):
#
#     s1_length = len(s1)
#     s2_length = len(s2)
#     print(s1_length)
#     print(s2_length)
#
#     new_string = ''
#
#     i = 0
#     while i < s1_length:
#
#         if s1[i: i + s2_length] == s2:
#             new_string += s3
#             i += s2_length
#
#         else:
#             new_string += s1[i]
#             i += 1
#
#     return new_string
#
#
# text = "I cats one cat"
# keyword = "cat"
# replcement="dog"
# newText = remove_all(text, keyword,replcement)
#
# print("Before:", text)
# print("After: ", newText)
#
#




(x)