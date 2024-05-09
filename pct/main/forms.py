from django import forms

# username=models.CharField(max_length=20)
#     first_name=models.CharField(max_length=20)
#     last_name=models.CharField(max_length=20)
#     email=models.EmailField()
#     password=models.CharField(max_length=20)
class registertable(forms.Form):
    username=forms.CharField(min_length=6,max_length=15)
    first_name=forms.CharField(min_length=6,max_length=15)
    Last_name=forms.CharField(min_length=6,max_length=15)
    email=forms.EmailField()
    password=forms.CharField(min_length=8,max_length=16,widget=forms.PasswordInput)
    confirm_password=forms.CharField(min_length=8,max_length=16,widget=forms.PasswordInput)

class logint(forms.Form):
    username=forms.CharField(min_length=6,max_length=15)
    password=forms.CharField(min_length=8,max_length=16,widget=forms.PasswordInput)