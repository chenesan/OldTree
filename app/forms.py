from django import forms

class QuestionsForm(forms.Form):
    division = forms.CharField(label='division', max_length=20)

class MessageForm(forms.Form):
    content = forms.CharField(label='content', max_length=20)
