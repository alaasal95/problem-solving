

# لعبة تحزير الكلمات, لكن باستخدام الحلقات, بحيث يظل البرنامج يطلب من المستخدم ادخال القيمة مادامت غير صحيحة


CorecttGuess=int(input('Please Enter your number='))

running=True

while (running==True):
      Guess=int(input('Enter Your Guessse='))
      if (CorecttGuess == Guess):
          print('You win.. ')
          running=False
      elif (CorecttGuess < Guess):
          print('Woring,your number bigger..!')
      elif (CorecttGuess > Guess):
          print('Woring,your number smallest..!')