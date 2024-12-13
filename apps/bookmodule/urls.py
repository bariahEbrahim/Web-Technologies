from django.urls import path  # type: ignore
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
    path('simple/query', views.simple_query, name='simple_query'), #lap7
    path('lookup/query', views.lookup_query, name='lookup_query'), #lap7
    path('lab8/task1', views.task1, name='task1'), #lab 8
    path('lab8/task2', views.task2, name='task2'),
    path('lab8/task3', views.task3, name='task3'),
    path('lab8/task4', views.task4, name='task4'),
    path('lab8/task5', views.task5, name='task5'),
    path('lab8/task7', views.task7, name='task7'),
    path('lab9_part1/listbook', views.list_book, name='list_book'), #lab 9
    path('lab9_part1/addbook', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
    path('lab9_part2/addbook', views.add_book_form, name='add_book_form'), #lab9 part2











]
