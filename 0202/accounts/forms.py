from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'gender', 'age', 'weekly_avg_reading_time', 'annual_reading_amount', 'profile_img', 'interested_genres')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'profile_img', 'interested_genres')