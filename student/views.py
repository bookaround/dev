from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from django import forms

from bookaround.models import Student, Recommendation_List, Want_Read_List, Am_Read_List, \
            Have_Read_List, Parent, Book, Author, Categories, Have_Read_List_Book_Membership, \
            Want_Read_List_Book_Membership, Am_Read_List_Book_Membership, Video_Review
from bookaround.forms import ParentLoginForm, StudentLoginForm, BookSearchForm, UploadReviewForm

#from apiclient.discovery import build
import json, requests


#move this into environmental variable and regenerate api key prior to beta
google_api_key = "AIzaSyDSdNiHGDTICCR9jve9nATFTGT0GMMs24U"

# probably get rid of this function
def student_login(request):
    return HttpResponseRedirect(reverse('student:home'))   

@login_required  #change to student_login_required
def home(request):
        template = loader.get_template('student/home.html')
        context = RequestContext(request, {
            })
        return HttpResponse(template.render(context))


    
@login_required    
def review(request):
    # Handle file upload
    if request.method == 'POST':
        form = UploadReviewForm(request.POST, request.FILES)
        if form.is_valid():
            video_review = Video_Review(video_file = request.FILES['file'])
            video_review.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('student:home'))  	
    else:
        form = UploadReviewForm() # A empty, unbound form

    # Load documents for the list page
    video_reviews = [] #Video_Review.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'student/upload_review.html',
        {'video_reviews': video_reviews, 'form': form},
        context_instance=RequestContext(request)
    )    

@login_required  #change to student_login_required  
def find(request):
    #student = Student.objects.get(username = request.session["username"]) #get rid of this
    
    if request.method == 'POST':
    
        #build the search query for google books API
        form = BookSearchForm(request.POST)
        q="q="     
        if form.validAndNotEmpty():
            if form.cleaned_data['title']:
                q = q+"intitle:"+form.cleaned_data['title']+"+"
            if form.cleaned_data['author']:
                q = q+"inauthor:"+form.cleaned_data['author']+"+"
            if form.cleaned_data['publisher']:
                q = q+"inpublisher:"+form.cleaned_data['publisher']+"+"
            if form.cleaned_data['subject']:
                q = q+"insubject:"+form.cleaned_data['subject']+"+"
            q = q[:-1]          # remove trailing '+' from query string
            
            
            #google api client library for python
            #service = build('books', 'v1', developerKey = google_api_key)
            #collection = service.volumes()
            #books_request = collection.list(q=q, maxResults = 40)     
            #response = books_request.execute()
            
            books_query = "https://www.googleapis.com/books/v1/volumes?"+q   
            response = requests.get(books_query).json()  
            print response


            #filter results
            results = []            
            
            #only show result if it has thumbnail
            for each in response['items']:
                try:
                    if each["volumeInfo"]["imageLinks"]["thumbnail"]: 
                        results.append(each)
                except:
                    pass

            
            template = loader.get_template('student/find_results.html')
            context = RequestContext(request, {
                'results' : results,
            })
            return HttpResponse(template.render(context))
        
    else:
        form = BookSearchForm()     
        
    rec_books = Recommendation_List.objects.get_or_create(student=request.user)[0].book.all()[0:3]
        
        
    template = loader.get_template('student/find.html')        
    context = RequestContext(request, {
        'bookSearchForm' : form,
        'rec_books': rec_books,     
        })
    return HttpResponse(template.render(context))             

    
#update this    
@login_required  #change to student_login_required
def bookshelf(request):

    am_read_books_list = Am_Read_List.objects.get_or_create(student=request.user)[0].book.all()[0:4]
    am_read_books = Book.objects.filter(am_read_list__student = request.user).order_by('-am_read_list_book_membership')[0:4]
    
    want_read_books_list = Want_Read_List.objects.get_or_create(student=request.user)[0]
    want_read_books = Book.objects.filter(want_read_list__student = request.user).order_by('-want_read_list_book_membership')[0:4]
    
    have_read_books_list = Have_Read_List.objects.get_or_create(student=request.user)[0]
    have_read_books = Book.objects.filter(have_read_list__student = request.user).order_by('-have_read_list_book_membership')[0:4]
    
        
    template = loader.get_template('student/bookshelf.html')
    context = RequestContext(request, {
        'am_read_books' : am_read_books,
        'want_read_books' : want_read_books,
        'have_read_books' : have_read_books,
        })
    return HttpResponse(template.render(context))         


#update this    
@login_required  #change to student_login_required     
def profile(request):
    template = loader.get_template('student/profile.html')
    context = RequestContext(request, {
        })
    return HttpResponse(template.render(context))  

#update this    
@login_required  #change to student_login_required  
def viewbook(request):
    student = Student.objects.get(username = request.session["username"])
    template = loader.get_template('student/viewbook.html')
    context = RequestContext(request, {
        'name' : student.first_name,
        'student_avatar' : student.avatar
        })
    return HttpResponse(template.render(context))    
	
		

	
@login_required  #change to student_login_required    
def process_results(request):
    """Function to take the books a child is interested in, query the Google Books API
    to populate our database with it if it isn't already there, then add the books to the 
    appropriate book lists"""
    
    #each of these lists are used later to add to the correct bookshelf
    am_read_list = []
    for each in request.POST.getlist("am_read_list"):
        am_read_list.append(each.split("/")[-1])

    want_read_list = []
    for each in request.POST.getlist("want_read_list"):
        want_read_list.append(each.split("/")[-1])

    have_read_list = []
    for each in request.POST.getlist("have_read_list"):
        have_read_list.append(each.split("/")[-1])

    full_list = set(am_read_list + want_read_list + have_read_list)  
    
    
    #google api client library for python
    #service = build('books', 'v1', developerKey = google_api_key)
    #collection = service.volumes()

    for google_id in full_list: #add book to our database if not already there 
        
        #check to see if the book is in our database yet. If not, query Google Books to add it
        try:
            theBook = Book.objects.get(google_id=google_id)
        except:
        
            #google api client library for python

            #books_request = collection.get(volumeId=google_id)     
            #response = books_request.execute()   
            
            response = requests.get('https://www.googleapis.com/books/v1/volumes/'+google_id).json()
            
            industID = {} #not all google books have industry data. Create a blank dictionary if it's not included in API response
            try:
                for each in  response["volumeInfo"]["industryIdentifiers"]:
                    industID[each["type"]] = each["identifier"]
            except:
                industID["ISBN_10"] = ""
                industID["ISBN_13"] = "" 

            imageLinks = {} #not all google books have image data. Create a blank dictionary if it's not included in API response
            try:
                x = response["volumeInfo"]["imageLinks"]     
                imageLinks["smallThumbnail"] = x.get("smallThumbnail", "")
                imageLinks["thumbnail"] = x.get("thumbnail", "")  
                imageLinks["small"] = x.get("small", "")                
                imageLinks["medium"] = x.get("medium", "")
                imageLinks["large"] = x.get("large", "")
                imageLinks["extraLarge"] = x.get("extraLarge", "")
            except:
                imageLinks["smallThumbnail"] = ""
                imageLinks["thumbnail"] = ""
                imageLinks["small"] = ""         
                imageLinks["medium"] = ""
                imageLinks["large"] = ""
                imageLinks["extraLarge"] = ""
                
            theBook = Book(   google_id= response["id"], \
                                        title = response["volumeInfo"].get("title",""), \
                                        publisher = response["volumeInfo"].get("publisher",""), \
                                        publishedDate =response["volumeInfo"].get("publishedDate",""), \
                                        description = response["volumeInfo"].get("description", ""), \
                                        pageCount = response["volumeInfo"].get("pageCount", 0), \
                                        language = response["volumeInfo"].get("language",""), \
                                        smallThumbnail = imageLinks["smallThumbnail"], \
                                        thumbnail = imageLinks["thumbnail"], \
                                        small = imageLinks["small"], \
                                        medium =  imageLinks["medium"], \
                                        large = imageLinks["large"], \
                                        extraLarge = imageLinks["extraLarge"], \
                                        ISBN_10 = industID["ISBN_10"], \
                                        ISBN_13 = industID["ISBN_13"], \
                                        )
            theBook.save()
            
            #   authors       
            if response["volumeInfo"].get("authors",False):            
                for each in  response["volumeInfo"]["authors"]:
                    try:
                        author = Author.objects.get(name=each)
                    except:
                        author = Author(name=each)
                        author.save()
                    theBook.authors.add(author)
 
            #  categories 
            if response["volumeInfo"].get("categories",False):
                for each in  response["volumeInfo"]["categories"]:
                    try:
                        category = Categories.objects.get(category=each)
                    except:
                        category = Categories(category=each)
                        category.save()
                    theBook.categories.add(category)    
                    
                    
        #Now that we are certain all books are in the database, add them to the appropriate lists
        if theBook.google_id in am_read_list:
            student_am_read_list = Am_Read_List.objects.get_or_create(student=request.user)[0]
            Am_Read_List_Book_Membership.objects.get_or_create(am_read_list = student_am_read_list, book = theBook)
                
        if theBook.google_id in want_read_list:
            student_want_read_list = Want_Read_List.objects.get_or_create(student=request.user)[0]
            Want_Read_List_Book_Membership.objects.get_or_create(want_read_list = student_want_read_list, book = theBook)
                
        if theBook.google_id in have_read_list:
            student_have_read_list = Have_Read_List.objects.get_or_create(student=request.user)[0]
            Have_Read_List_Book_Membership.objects.get_or_create(have_read_list = student_have_read_list, book = theBook)


    return HttpResponseRedirect(reverse('student:bookshelf'))  	
	
	