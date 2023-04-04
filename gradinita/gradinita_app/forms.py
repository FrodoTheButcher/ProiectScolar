from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Profile , Kids , absente_elev , motivari_elev

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            widget = field.widget
            widget.attrs.update({'class': 'input'})
            if 'placeholder' in widget.attrs:
                del widget.attrs['placeholder']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'last_name', 'profile_image', 'username', 'kid', 'email']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget = field.widget
            widget.attrs.update({'class': 'input', 'placeholder': ' '})




class EditPasswordForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1','password2','email']
        def __init__(self,*args,**kwargs):
            super(CustomUserCreationForm,self).__init__(*args,**kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})


class KidsForm(ModelForm):
    class Meta:
        model = Kids
        fields = ['name','full_name','last_name','group','age','key']
        def __init__(self,*args,**kwargs):
            super(CustomUserCreationForm,self).__init__(*args,**kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})

class absente_elevForm(ModelForm):
    class Meta:
        model = absente_elev
        fields = ['numar','data']

class motivari_elevForm(ModelForm):
    class Meta:
        model = motivari_elev
        fields = ['numar','data']