from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals



 #############################
#User Profile related models
#############################
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")

    # The additional attributes we wish to include.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)    
    avatar = models.CharField(max_length=30, default="user2.png")
    
    def delete_user(self):
        try:
            self.user
        except User.DoesNotExist:
            pass
        else:
            self.user.delete()    
        
    def __str__(self):
        return self.user.username+ " UserProfile"
        
        
class EducatorProfile(models.Model):
    #UserProfile for Educators
    user_profile = models.OneToOneField(UserProfile, related_name="educator_profile")

    # The additional attributes we wish to include.
    school_name = models.CharField(max_length=100)
    school_year = models.CharField(max_length=10)
    classroom_number = models.CharField(max_length=10)

    def __str__(self):
        return self.user_profile.user.username + " EducatorProfile"

    def delete_user(self):
        try:
            self.user_profile.user
        except User.DoesNotExist:
            pass
        else:
            self.user_profile.user.delete_user()       
        
        
class StudentProfile(models.Model):
    #UserProfile for Educators
    user_profile = models.OneToOneField(UserProfile, related_name="student_profile")

    # The additional attributes we wish to include.
    plaintext_pw = models.CharField(max_length=100) #teachers can create, view, and update passwords for kids, requiring us to store it as plaintext in the database
    lexile_score = models.IntegerField()
    points = models.IntegerField()
    school_name = models.CharField(max_length=100)
    school_year = models.CharField(max_length=10)
    classroom_number = models.CharField(max_length=10)
    educator = models.ForeignKey(User)

    def __str__(self):
        return self.user_profile.user.username + " StudentProfile"  
        
    def delete_user(self):
        try:
            self.user_profile.user
        except User.DoesNotExist:
            pass
        else:
            self.user_profile.user.delete_user()             
    
class ParentProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, related_name="parent_profile")
    students = models.ManyToManyField(StudentProfile)
    def __str__(self):
        return self.user_profile.user.username + " ParentProfile"  
        
    def delete_user(self):
        try:
            self.user_profile.user
        except User.DoesNotExist:
            pass
        else:
            self.user_profile.user.delete_user()             

        
        
#to delete and replace with Users and ParentProfiles
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    avatar = models.CharField(max_length=30)
    lexile_score = models.IntegerField()
    points = models.IntegerField()
    def __str__(self):
        return self.first_name +" "+ self.last_name   
        
class Parent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, null = True)    
    email = models.CharField(max_length=30)
    students = models.ManyToManyField(Student)
    username = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.first_name +" "+ self.last_name
        
#To delete and replace with Users and StudentProfiles
 
        
        
 #############################
#book and book related models
#############################
        
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
        
class Categories(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category
    
class Book(models.Model):
    google_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    authors =models.ManyToManyField(Author)
    publisher = models.CharField(max_length=100, blank=True, default="")
    publishedDate = models.CharField(max_length = 100, blank=True, default="")
    description = models.TextField(blank = True, default="")
    pageCount = models.IntegerField()
    categories =models.ManyToManyField(Categories)
    language = models.CharField(max_length=100, blank=True, default="")
    ISBN_10 = models.CharField(max_length=100, blank=True, default="")
    ISBN_13 = models.CharField(max_length=100, blank=True, default="")
    smallThumbnail = models.URLField(max_length=600, blank=True, default="")
    thumbnail = models.URLField(max_length=600, blank=True, default="")
    small = models.URLField(max_length=600, blank=True, default="")
    medium = models.URLField(max_length=600, blank=True, default="")
    large = models.URLField(max_length=600, blank=True, default="")
    extraLarge = models.URLField(max_length=600, blank=True, default="")
    def __str__(self):
        return self.title    

        
#############################
#book list models and ordering models
#############################
class Recommendation_List(models.Model):
    student = models.ForeignKey(User)
    book = models.ManyToManyField(Book, through='Recommendation_List_Book_Membership')
    def __str__(self):
        return self.student.first_name +" "+ self.student.last_name +" rec list"  
        
class Recommendation_List_Book_Membership(models.Model):
    recommendation_list = models.ForeignKey(Recommendation_List)
    book = models.ForeignKey(Book)
    date_added =models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ('date_added',)
    def __str__(self):
        return self.student.username +" am read" + self.book.title
        
        
class Am_Read_List(models.Model):
    student = models.ForeignKey(User)
    book = models.ManyToManyField(Book, through='Am_Read_List_Book_Membership')
    def __str__(self):
        return self.student.username +" am read"

class Am_Read_List_Book_Membership(models.Model):
    am_read_list = models.ForeignKey(Am_Read_List)
    book = models.ForeignKey(Book)
    date_added =models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ('date_added',)
    def __str__(self):
        return self.student.username +" am read" + self.book.title
        

class Want_Read_List(models.Model):
    student = models.ForeignKey(User)
    book = models.ManyToManyField(Book, through='Want_Read_List_Book_Membership')
    def __str__(self):
        return self.student.username +" want read"

class Want_Read_List_Book_Membership(models.Model):
    want_read_list = models.ForeignKey(Want_Read_List)
    book = models.ForeignKey(Book)
    date_added =models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ('date_added',)
    def __str__(self):
        return self.student.username +" want read" + self.book.title
        
        
class Have_Read_List(models.Model):
    student = models.ForeignKey(User)
    book = models.ManyToManyField(Book, through='Have_Read_List_Book_Membership')
    def __str__(self):
        return self.student.username +" have read"
         
class Have_Read_List_Book_Membership(models.Model):
    have_read_list = models.ForeignKey(Have_Read_List)
    book = models.ForeignKey(Book)
    date_added =models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ('date_added',)
    def __str__(self):
        return self.student.username +" have read" + self.book.title
    
    
    
    
    
    
    
    
#############################    
#'work in progress' models below (not used for anything)
#############################

class Book_Rating(models.Model):
    """a model to keep track of what ratings a student has given to a book"""
    student = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    rating = (
        ('1', 'Did not like'),
        ('2', 'Liked a little'),
        ('3', 'Liked'),
        ('4', 'Liked a lot'),
    )
    updatestamp = models.DateField(auto_now=True)
    createdstamp = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.student.first_name +"-"+ self.book.title       

        
        
        
class Featured_Recommendations(models.Model):
    """a model keeping track of books that a parent might want to recommend to their child"""
    parent = models.ForeignKey(Parent)
    student = models.ForeignKey(Student)
    book = models.ForeignKey(Book)
    def __str__(self):
        return self.parent.username +" for "+ self.student.username  


        
        

class Video_Review(models.Model):
#    student = models.ForeignKey(Student)
 #   book = models.CharField(max_length = 60)
  #  RATING_CHOICE = (
  #      (1, 'Didn\'t Like'),
  #      (2, 'Liked A Little'),
   #     (3, 'Liked'),
    #    (4, 'Liked A Lot'),
    #)
    #rating = models.IntegerField(
    #                                  choices=RATING_CHOICE,
    #                                  default=1)
    createdstamp = models.DateField(auto_now_add=True)
    updatestamp = models.DateField(auto_now=True)
    video_file = models.FileField(upload_to="video")         
    def __str__(self):
        return self.student.username +" reviews "+ self.book.title  
