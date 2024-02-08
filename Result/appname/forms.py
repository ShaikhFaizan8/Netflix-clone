from django import forms

class MarksForm(forms.Form):
    CPP = forms.IntegerField(label='Cpp Marks')
    PYTHON = forms.IntegerField(label='Python Marks')
    JAVA = forms.IntegerField(label='Java Marks')
    ENGLISH = forms.IntegerField(label='English Marks')
    HINDI = forms.IntegerField(label='Hindi Marks')
    MARATHI = forms.IntegerField(label='Marathi Marks')
    SCIENCE = forms.IntegerField(label='Science Marks')
