
import os

def populate():
#*******
#students
#*******

    student = Student(first_name="Newton", last_name="Penguin", username="newtonPenguin", password="np", email="newton@bookaround.com", avatar="user2.png", lexile_score="70", points="3",)
    student.save()
    student = Student(first_name="Jose", last_name="Ortiz", username="JORT", password="jo", email="Jose@bookaround.com", avatar="user2.png", lexile_score="70", points="3",)
    student.save()
    student = Student(first_name="Esperanza", last_name="Reyes", username="EREYES", password="er", email="Esperanza@bookaround.com", avatar="user2.png", lexile_score="95", points="6",)
    student.save()
    student = Student(first_name="Saya", last_name="Jones", username="SJONES", password="sj", email="Saya@bookaround.com", avatar="user2.png", lexile_score="150", points="1",)
    student.save()
    student = Student(first_name="Daezon", last_name="Smith", username="DSMITH", password="ds", email="Daezon@bookaround.com", avatar="user2.png", lexile_score="200", points="8",)
    student.save()
    student = Student(first_name="Clint", last_name="Barnes", username="CBARNES", password="cb", email="Clint@bookaround.com", avatar="user2.png", lexile_score="225", points="23",)
    student.save()
    student = Student(first_name="Drew", last_name="Cutchin", username="ACUTCHIN", password="ac", email="Drew@bookaround.com", avatar="user2.png", lexile_score="300", points="14",)
    student.save()
    student = Student(first_name="Tim", last_name="Zitto", username="TZITTO", password="tz", email="Tim@bookaround.com", avatar="user2.png", lexile_score="350", points="7",)
    student.save()
    student = Student(first_name="Brianna", last_name="Young", username="BYOUNG", password="by", email="Brianna@bookaround.com", avatar="user2.png", lexile_score="500", points="6",)
    student.save()
    student = Student(first_name="Ben", last_name="Catania", username="BCATANIA", password="bc", email="Ben@bookaround.com", avatar="user2.png", lexile_score="320", points="27",)
    student.save()
    student = Student(first_name="James", last_name="Alfred", username="JALFRED", password="ja", email="James@bookaround.com", avatar="user2.png", lexile_score="140", points="1",)
    student.save()
    student = Student(first_name="Art", last_name="Moore", username="AMOORE", password="am", email="Art@bookaround.com", avatar="user2.png", lexile_score="130", points="7",)
    student.save()
    student = Student(first_name="Joe", last_name="King", username="JKING", password="jk", email="Joe@bookaround.com", avatar="user2.png", lexile_score="500", points="17",)
    student.save()
    student = Student(first_name="Brendan", last_name="Chen", username="BCHEN", password="bc", email="Brendan@bookaround.com", avatar="user2.png", lexile_score="80", points="29",)
    student.save()
    student = Student(first_name="Tom", last_name="Kemper", username="TKEMPER", password="tk", email="Tom@bookaround.com", avatar="user2.png", lexile_score="100", points="3",)
    student.save()
    student = Student(first_name="Mike", last_name="Newton", username="MNEWTON", password="mn", email="Mike@bookaround.com", avatar="user2.png", lexile_score="120", points="8",)
    student.save()
    student = Student(first_name="Ashley", last_name="Donnelly", username="ADONNELLY", password="ad", email="Ashley@bookaround.com", avatar="user2.png", lexile_score="250", points="6",)
    student.save()
    student = Student(first_name="Amanda", last_name="Long", username="ALONG", password="al", email="Amanda@bookaround.com", avatar="user2.png", lexile_score="300", points="3",)
    student.save()
    student = Student(first_name="Kendra", last_name="Thompson", username="KTHOMPSON", password="kt", email="Kendra@bookaround.com", avatar="user2.png", lexile_score="400", points="11",)
    student.save()
    student = Student(first_name="Tina", last_name="Giffin", username="TGIFFIN", password="tg", email="Tina@bookaround.com", avatar="user2.png", lexile_score="370", points="3",)
    student.save()



    #*******
    #parents
    #*******

    parent = Parent(first_name = "tammy", last_name = "Penguin", surname ="Elder", email ="tammy@bookaround.com", username = "ParentPenguin")				
    parent.save()	
    parent.students.add(Student.objects.get( username = "newtonPenguin"))	
    parent = Parent(first_name = "parent", last_name = "Ortiz", surname ="Elder", email ="parent@bookaround.com", username = "ParentOrtiz")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "JORT"))				
    parent = Parent(first_name = "parent", last_name = "Reyes", surname ="Elder", email ="parent@bookaround.com", username = "ParentReyes")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "EREYES"))				
    parent = Parent(first_name = "parent", last_name = "Jones", surname ="Elder", email ="parent@bookaround.com", username = "ParentJones")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "SJONES"))
    parent = Parent(first_name = "parent", last_name = "Smith", surname ="Elder", email ="parent@bookaround.com", username = "ParentSmith")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "DSMITH"))
    parent = Parent(first_name = "parent", last_name = "Barnes", surname ="Elder", email ="parent@bookaround.com", username = "ParentBarnes")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "CBARNES"))				
    parent = Parent(first_name = "parent", last_name = "Cutchin", surname ="Elder", email ="parent@bookaround.com", username = "ParentCutch")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "ACUTCHIN"))			
    parent = Parent(first_name = "parent", last_name = "Zitto", surname ="Elder", email ="parent@bookaround.com", username = "ParentZitto")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "TZITTO"))
    parent = Parent(first_name = "parent", last_name = "Young", surname ="Elder", email ="parent@bookaround.com", username = "ParentYoung")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "BYOUNG"))
    parent = Parent(first_name = "parent", last_name = "Catania", surname ="Elder", email ="parent@bookaround.com", username = "ParentCatania")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "BCATANIA"))				
    parent = Parent(first_name = "parent", last_name = "Alfred", surname ="Elder", email ="parent@bookaround.com", username = "ParentAlfred")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "JALFRED"))
    parent = Parent(first_name = "parent", last_name = "Moore", surname ="Elder", email ="parent@bookaround.com", username = "ParentMoore")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "AMOORE"))
    parent = Parent(first_name = "parent", last_name = "King", surname ="Elder", email ="parent@bookaround.com", username = "ParentKing")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "JKING"))
    parent = Parent(first_name = "parent", last_name = "Chen", surname ="Elder", email ="parent@bookaround.com", username = "ParentChen")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "BCHEN"))
    parent = Parent(first_name = "parent", last_name = "Kemper", surname ="Elder", email ="parent@bookaround.com", username = "ParentKemper")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "TKEMPER"))
    parent = Parent(first_name = "parent", last_name = "Newton", surname ="Elder", email ="parent@bookaround.com", username = "ParentNewton")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "MNEWTON"))
    parent = Parent(first_name = "parent", last_name = "Donnelly", surname ="Elder", email ="parent@bookaround.com", username = "ParentDonnelly")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "ADONNELLY"))
    parent = Parent(first_name = "parent", last_name = "Long", surname ="Elder", email ="parent@bookaround.com", username = "ParentLong")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "ALONG"))
    parent = Parent(first_name = "parent", last_name = "Thompson", surname ="Elder", email ="parent@bookaround.com", username = "ParentThompson")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "KTHOMPSON"))
    parent = Parent(first_name = "parent", last_name = "Giffin", surname ="Elder", email ="parent@bookaround.com", username = "ParentGiffin")				
    parent.save()				
    parent.students.add(Student.objects.get( username = "TGIFFIN"))

# Start execution here!
if __name__ == '__main__':
    print "Starting Bookaround population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookaround.settings')
    from bookaround.models import Student, Parent
    populate()