from django.contrib.auth.models import User
from django import forms
from bookaround.models import UserProfile, EducatorProfile, StudentProfile, Video_Review


class ParentLoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'initial':'tammyPenguin', 'value':'ParentPenguin'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control input-lg', 'initial':'password', 'value':'password', 'disabled':'True'}))

class StudentLoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'initial':'newtonPenguin', 'value':'newtonPenguin'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control input-lg', 'initial':'password', 'value':'password', 'disabled':'True'}))

	
class BookSearchForm(forms.Form):
    title=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'initial':'Search Title'}), required=False)
    author=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'initial':'Search Title'}), required=False)	
    publisher=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'initial':'Search Title'}), required=False)
    subject=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'initial':'Search Title'}), required=False)
     
    def validAndNotEmpty(self):
        """returns True if all fields are valid and at least one isn't empty. Returns false otherwise"""
        valid = super(BookSearchForm, self).is_valid()
        if not valid:
            return valid
            
        if len( self.cleaned_data['title'] + \
                  self.cleaned_data['author'] + \
                  self.cleaned_data['publisher'] + \
                  self.cleaned_data['subject']
                  ) == 0:
            return False
            
        return True
        
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name')
        
class EducatorProfileForm(forms.ModelForm):
    class Meta:
        model = EducatorProfile
        fields = ('school_name', 'school_year', 'classroom_number')        

    
class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)       
        
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('school_name', 'school_year', 'classroom_number', 'lexile_score', 'points', 'plaintext_pw')         
    
    
#this class is a work in progress (i.e. doesn't do anything)   
class UploadReviewForm(forms.Form):
 #   book_title = forms.CharField(max_length=50)
  #  book_review = forms.CharField(max_length=50)    
    file = forms.FileField(        
        label='Select a file',
        help_text='max. 42 megabytes')   
  #  class Meta:
  #      model = Video_Review  
  #      fields = ('student', 'rating', 'book', 'filename')
    
    
    



