from django.shortcuts import render # type: ignore
# Create your views here.
from django.http import HttpResponse # type: ignore

# def index(request):
#     name = request.GET.get("name") or "world!" #add this line
#     return render(request, "bookmodule/index.html" , {"name": name}) #your render line
def index(request):
 return render(request, "bookmodule/index.html")
def list_books(request):
 books = [
        {'id': 1, 'title': 'Internet & World Wide Web How to Program'},
        {'id': 2, 'title': 'C++ How to Program, Late Objects Version'},
        {'id': 3, 'title': 'Images in Another Folder'},
    ]
 return render(request, 'bookmodule/list_books.html', {'books': books})
#  return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')

def one_book(request):
    return render(request, "bookmodule/one_book.html")


def index2(request, val1 = 0): #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)


def html5_links(request):
    return render(request, 'bookmodule/links.html')

def text_formatting(request):
    return render(request, 'bookmodule/formatting.html')

def html5_listing(request):
    return render(request, 'bookmodule/listing.html')


def html5_table(request):
    return render(request, 'bookmodule/table.html')


def search_books(request):
    books = []
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        is_title = request.POST.get('option1')
        is_author = request.POST.get('option2')

        # Retrieve the book list
        all_books = __getBooksList()

        # Filter books based on the form input
        for book in all_books:
            contains = False
            if is_title and keyword in book['title'].lower():
                contains = True
            if is_author and keyword in book['author'].lower():
                contains = True

            if contains:
                books.append(book)

    return render(request, 'bookmodule/search.html', {'books': books})


def __getBooksList():
    return [
        {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'},
        {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'},
        {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'},
    ]


