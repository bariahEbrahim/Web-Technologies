from django.urls import path # type: ignore
from . import views  # Import the views from the current directory

urlpatterns = [
    path('', views.index),  # Map the root URL of bookmodule to the 'index' view
    path('index2/<int:val1>/', views.index2),  # Map '/index2/' to 'index2' view
    path('<int:bookId>', views.viewbook),
    path('html5/links/', views.html5_links),  # New path for Task 1
    path('html5/text/formatting/', views.text_formatting),  # New URL for Task 2
    path('html5/listing/', views.html5_listing),  # New URL for Task 3
    path('html5/table/', views.html5_table),  # New URL for Task 4

    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('one_book/', views.one_book, name="books.one_book"),  # Static path for one_book
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('search', views.search_books, name='search_books'), #lap6  
]
