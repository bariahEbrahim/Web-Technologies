from django.urls import path
from . import views  # Import the views from the current directory

urlpatterns = [
    path('', views.index),  # Map the root URL of bookmodule to the 'index' view
    path('index2/<int:val1>/', views.index2),  # Map '/index2/' to 'index2' view
    path('<int:bookId>', views.viewbook)

]
