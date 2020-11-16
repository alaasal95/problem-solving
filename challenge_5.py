

'''

---->Ex:// It asks users to enter text and then enter one letter.
Then the program that prints a place for this letter in the text.

Example: If he kills a 24-gauge fire on the text "Harmash is the
          best site for learning programming" and then enter the
          letter "Harm to print the following result when running."

'''


text=input('enter the text:')
enter=input('enter character:')
text_length=len(text)
print('text_length:',text_length)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
i=0
while(i<text_length):
    if(text[i]==enter):
        print(text[i],'index is:',i)
    i=i+1
