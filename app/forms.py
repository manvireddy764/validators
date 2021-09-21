from django import forms

def check_for_alpa(value):
    if value[0].lower()=='m':
        raise forms.ValidationError('Name should not start with m')
def check_for_len(value):
    if len(value)>6:
        raise forms.ValidationError('Name must be lessthan 6 characters')

def check_for_age(value):
    if value<18 or value>45:
        raise forms.ValidationError('age is must be in between 18 & 45')

class StudentForm(forms.Form):
    Name=forms.CharField(max_length=100,validators=[check_for_alpa,check_for_len])
    Age=forms.IntegerField(validators=[check_for_age])
    Email=forms.EmailField(max_length=100)
    ReEnterEmail=forms.EmailField(max_length=100)


    def clean(self):
        e=self.cleaned_data['Email']
        r=self.cleaned_data['ReEnterEmail']
        if e!=r:
            raise forms.ValidationError('entered emails are not same')