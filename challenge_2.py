
'''
 By defining a function called ReplaceAll, its idea is to search the text for a specific part (word or phrase) and
  replace it with another part.
When summoning her, we must pass three texts to her. The first represents a regular text,
 the second represents the component we want to search for,
 and the third represents the component we want to place in place of the second part.
In the end, a copy of the first text should be returned after the part we searched for has been replaced by
the part we want to place it in.
Then try this function in the program.

Example: Using the ReplaceAll () function we can replace every word "cat" in the text "I like cats. I have one cat.
         " In the word "dog" and then you will return to us the text "I like dogs. I have one dog."
'''






def count_occurrences(s1, s2,s3):

    counter = 0

    for i in range(0, len(s1) ):
        if s1[ i:i + len(s2)] == s2:
           x=s1.replace(s1[ i:i + len(s2)],s3)

    print(x)
   # return x

text = input('Enter any text: ')
keyword = input('Enter word to search occurrences: ')
change_word=input('enter changing word:')
result = count_occurrences(text, keyword,change_word)

#print("Total occurrences of '" + keyword + "' is: " + str(result))

print('s=',len(text))

print('s2=',len(keyword))





########################
##-->anoher solution
#######################



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


