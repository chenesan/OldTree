from django import forms

class QuestionsForm(forms.Form):
    gender = forms.CharField(label='gender', max_length=20)
