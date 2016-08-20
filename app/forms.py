from django import forms

class QuestionsForm(forms.Form):
    gender = forms.CharField(label='gender', max_length=20)

class MessageForm(forms.Form):
    content = forms.CharField(label='content', max_length=20)
