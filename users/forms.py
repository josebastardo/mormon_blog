"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile

class profileForm(forms.ModelForm): 
	class Meta: 
		model = Profile 
		fields = ('user','photo')


class SignupForm(forms.Form):
    """Sign up form."""

    email = forms.CharField(
        min_length=6,
        max_length=40,
        widget=forms.EmailInput()
    )
    username = forms.CharField(
        min_length=6,
        max_length=30,
        widget=forms.TextInput()
    )

   # photo = forms.ImageField(upload_to='users/pictures',default= 'user/pictures/perfilsinfoto.png')
    #    widget=forms.ImageFieldInput())
   
    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput()
    )
   
   

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()



