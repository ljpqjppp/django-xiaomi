from django import forms
from django.contrib.auth import get_user_model
from xiaomi_users.models import UserPhoneComment


class UserLogin(forms.Form):
    name = forms.CharField(max_length=20, min_length=3)
    pwd = forms.CharField(max_length=255, min_length=6, widget=forms.PasswordInput())


MyUser = get_user_model()
class RegForm(forms.ModelForm):
    class Meta:
        model = MyUser
        # fields = '__all__'  # 验证所有字段
        fields = ('username', 'password')
        widgets = {
            'password':forms.PasswordInput()
        }
        help_texts = {
            'username':(''),
            'password':(''),
        }


class UserPhoneCommentForm(forms.ModelForm):
    class Meta:
        model = UserPhoneComment
        fields = ('user', 'phone', 'context')