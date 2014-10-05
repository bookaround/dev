from django.contrib import admin
from bookaround.models import Student, Book, Parent, Recommendation_List, \
	Am_Read_List, Want_Read_List, Have_Read_List, Featured_Recommendations, \
	Video_Review, UserProfile, EducatorProfile, StudentProfile, Have_Read_List_Book_Membership



# Register your models here.
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Parent)
admin.site.register(Recommendation_List)
admin.site.register(Am_Read_List)
admin.site.register(Want_Read_List)
admin.site.register(Have_Read_List)
admin.site.register(Featured_Recommendations)
admin.site.register(Video_Review)
admin.site.register(UserProfile)
admin.site.register(EducatorProfile)
admin.site.register(StudentProfile)
admin.site.register(Have_Read_List_Book_Membership)