

def Alaa(a1,b1,c1):
    print('<----- اكبر شركات السيارت حول العالم ----->')
    print('1.Aston Martin,2.Alfa Romeo,3.Infiniti')
    name=int(input('enter your Choice='))

    if (name==1):
        print(a1)
        print('تعتبر شركة آستون مارتن لاجوندا المحدودة شركة بريطانية \n'
              'لصناعة السيارات الرياضية الفاخرة،ومقرها في قرية غايدون،\n'
              ' بمقاطعة وركشير. واشتق اسم الشركة من اسم أحد المؤسسين، \n'
              'ليونيل مارتن،وسباق هضبة آستون الذي كان يقام بالقرب من \n'
              'آستون كلينتون في بوكينغامشيري\n')
    elif(name==2):
        print(b1)
        print('هي شركة إيطالية لصناعة السيارات. تأسست في العام 1910.\n'
              ' تملكتها فيات جروب منذ 1986 وسابقا كانت تسمى (A.L.F.A)\n'
              ' وهي اختصارا ل (Anonima Lombarda Fabbrica Automobili).\n')
    elif(name==3):
        print(c1)
        print('هي قسم السيارات الفخمة من مصنع السيارات الياباني نيسان موتورز،\n'
              ' بدأت مبيعاتها عام 1989 في شمال أمريكا يعتبر المنافس الأبرز لإنفينيتي\n'
              ' المصنع الياباني لكزس بدأت إنفينيتي ببيع السيارات رسمياً 8 نوفمبر 1989\n'
              ' في أمريكا الشمالية وكذلك تباع في الشرق الأوسط وكوريا الجنوبية وروسيا\n'
              ' والتايوان والصين وأوكرانيا وكذلك دخلت في الأسواق الأوربية أواخر عام 2008\n'
              ' والشركة الآن تملك أكثر من 230 وكيل لبيع السيارات في 15 دولة.\n'
              'الاسم إنفينيتي لم يستعمل في اليابان إطلاقاً وقد بيعت منتجاتها تحت اسم نيسان موتورز.\n')


Alaa(a1='Aston Martin',b1='Alfa Romeo',c1='Infiniti')