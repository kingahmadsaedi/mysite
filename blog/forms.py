from django import forms
from blog.models import Comment
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):# form model way
    #captcha = CaptchaField()
    class Meta:
        model=Comment()
        fields=['post','name','subject','message','email']
