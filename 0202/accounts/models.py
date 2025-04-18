from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    weekly_avg_reading_time = models.PositiveIntegerField(blank=True, null=True, help_text='분 단위')
    annual_reading_amount = models.PositiveIntegerField(blank=True, null=True, help_text='권 단위')
    profile_img = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    interested_genres = models.TextField(blank=True, help_text='콤마로 구분된 문자열 장르 목록')

    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='UserFollowing',
        related_name='followers',
        blank=True
    )

class UserFollowing(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_set')

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f'{self.from_user} follows {self.to_user}'
