from django.db import models
from django.conf import settings


class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=20)
    description = models.TextField()
    customer_review_rank = models.FloatField()
    author = models.CharField(max_length=15)
    author_profile_img = models.ImageField(upload_to='author_profiles/', blank=True, null=True)
    author_info = models.TextField(blank=True, null=True)
    author_works = models.TextField(blank=True, null=True)
    cover_img = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    audio_file = models.FileField(upload_to='audio_books/', blank=True, null=True)

    def __str__(self):
        return self.title

class Thread(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='threads')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='threads')
    title = models.CharField(max_length=200)
    content = models.TextField()
    reading_date = models.DateField()
    cover_img = models.ImageField(upload_to='thread_covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_threads', blank=True, through='ThreadLike')

    def __str__(self):
        return f'{self.title} - {self.user}'

class ThreadLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'thread')

    def __str__(self):
        return f'{self.user} likes {self.thread}'
