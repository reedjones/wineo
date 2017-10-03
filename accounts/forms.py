__author__ = 'reed'


from profiles.models import Profile
from django import forms

class RegistrationForm(forms.Form):
      """
      part one
      """
      name = forms.CharField()
      nick = forms.CharField(max_length=60, min_length=2)
      email = forms.EmailField()
      description = forms.CharField(required=False)
      password1 = forms.CharField()
      password2 = forms.CharField()

      def clean(self):
          cleaned_data = super(RegistrationForm, self).clean()
          nicks = [profile.nick for profile in Profile.objects.all()]
          n = cleaned_data['nick']
          if n in nicks:
              raise forms.ValidationError("The nick {0} is already taken".format(n))

          if cleaned_data['password1'] != cleaned_data['password2']:
              raise forms.ValidationError("Passwords don't match")


class ImageForm(forms.Form):
    image = forms.ImageField()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()