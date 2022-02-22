from django.contrib.auth.models import User
from .models import SystemUser


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', )


class SystemUserForm(forms.ModelForm):
    class Meta:
        model = SystemUser
        fields = ('user_type', 'user_mobile', 'user_gender', )
