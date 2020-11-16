

'''

 EX://--->define method and when we calling this method we
          gave it to text,and it return to us a copy from
          the first text don't have on the second text
          example:==> text_1="I like cats. I have one cat."
                      text_2="cat"
                      result="I like s. I have one."

'''






def count_occurrences(s1, s2):

    counter = 0

    for i in range(0, len(s1) ):
        if s1[ i:i + len(s2)] == s2:
           x=s1.replace(s1[ i:i + len(s2)],'')

    print(x)
   # return x

text = input('Enter any text: ')
keyword = input('Enter word to search occurrences: ')

result = count_occurrences(text, keyword)

#print("Total occurrences of '" + keyword + "' is: " + str(result))

print('s=',len(text))

print('s2=',len(keyword))



