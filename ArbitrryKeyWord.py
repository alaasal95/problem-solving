





def Alaa(**boy):
    print('<---- اكبر شركات الادوية في العالم ---->')
    name=int(input('Enter your choice='))

    if(name==1):
        print(boy['a1'])

        print('هي شركة أدوية أمريكية رائدة يقع مقرها في مدينة نيويورك،\n '
              ' وتتخصص في أربعة مجالات رئيسية للعلاج هي الأورام والقلب\n'
              'والقلب والأوعية الدموية والمناعة والتليف .\n'
              '  بلغت إيرادات الشركة 22.6 مليار دولار عام 2018،\n '
              'ويرجع نمو الشركة القوي خلال ذلك العام إلى نجاح دواء علاج السرطان\n '
              ')أوبديفو( ودواء )إيليكيس( لعلاج تجلط الدم.\n')

    elif(name==2):
        print(boy['a2'])

        print('تتخصص هذه الشركة البريطانية في مجموعة كبيرة من مجالات العلاج،\n'
              'لكنها ناجحة بشكل خاص في أدوية علاج فيروس نقص المناعة المكتسبة \n'
              '(الإيدز) والجهاز التنفسي واللقاحات.شهدت )جلاكسو سميث كلاين( زيادة في\n'
              'الإيرادات بنسبة 2% عام 2018 مقارنة بعام 2017،بلغت إيراداتها العام\n'
              'الماضي 23 مليار دولار، كما زادت مبيعاتها بفضل نجاح أدوية نقص المناعة\n'
              'المكتسبة )تيفيكاي( و)تريوميك( وجهاز الاستنشاق )إليبتا( لعلاج الربو.\n'
              )

    elif(name==3):
        print(boy['a3'])

        print('هي شركة أدوية أمريكية يقع مقرها في كاليفورنيا، وتتخصص في تطوير أدوية جديدة \n'
              'مع التركيز على أمراض القلب والأوعية الدموية والعظام والأورام والكلى والالتهابات.\n'
              'حققت الشركة إيرادات بلغت 23.7 مليار دولار العام الماضي، وقد باتت تأتي في قائمة\n'
              'أفضل 10 شركات أدوية بشكل ثابت ، ويرجع ذلك إلى نجاح العديد من منتجاتها بما في ذلك دواء\n'
              '(ريباثا) (بزيادة سنوية بنسبة 72%),و(%)، و)بلينكيتو( بنسبة 31%، و)بروليا( بنسبة 16%.)')


    elif(name==4):
        print(boy['a4'])

        print('شهدت شركة الأدوية الأمريكية )أب في( زيادة في الإيرادات بنسبة 16.2% عام 2018 \n'
              'مقارنة بعام 2017، وقد بلغت إيراداتها العام الماضي 32.8 مليار دولار.\n'
              ' وتنتج الشركة مجموعة كبيرة من الأدوية لعلاج عدة أمراض بما في ذلك الأمراض الجلدية\n '
              'وأمراض الجهاز العصبي والجهاز الهضمي، ويعزز مبيعات الشركة دواء(هيوميرا)و(إمبروفيكا)\n'
              'وهو أحد أهم أدوية السرطان الآن.\n')



Alaa(a1='GlaxoSmithKline',a2='GlaxoSmithKline',a3=' Amgen',a4='AbbVie')