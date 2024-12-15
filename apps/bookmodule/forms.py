from django import forms
#from .models import Book , Student, Address # lab 10 task 1
from .models import Book ,  Student2, Address2, Gallery #lab 10 task 2



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']

#lab 10 task 1

# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = ['city']

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['name', 'age', 'address']

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']

    addresses = forms.ModelMultipleChoiceField(
        queryset=Address2.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['name', 'image']

