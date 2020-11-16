
import sqlite3

def main():
    db=sqlite3.connect('information.db')
    db.row_factory=sqlite3.Row   #يقوم بتحيل البيانات الى قاموس من اجل قراءتها في دالة الفور لوب
    db.execute('create table if not exists Admin(Name text,Age int)')
    db.execute('insert into Admin(Name,Age) values (?,?)',('Hussain',26))
    db.execute('insert into Admin(Name,Age) values (?,?)', ('hassan', 22))
    db.execute('insert into Admin(Name,Age) values (?,?)', ('zahraa', 16))
    db.execute('delete from Admin where Name="hassan" ')
    db.execute('Update Admin set Age=7 where Name="zahraa"')
    db.commit()
    #قراءة بينات من الجدول
    cusror=db.execute('select * from Admin')
    for row in cusror:
        print('Name:{},Age:{}'.format(row['Name'],row['Age']))

if __name__ == '__main__':main()
