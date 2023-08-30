from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm

# class userloginform(AuthenticationForm):
#     class Meta:
#         model=User
#user creation form django builtin
class usercform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', ]