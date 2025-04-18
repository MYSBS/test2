from django import forms
from .models import Book, Thread

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'description', 'customer_review_rank',
            'author', 'author_profile_img', 'author_info', 'author_works',
            'cover_img', 'audio_file'
        ]

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content', 'reading_date', 'cover_img']
