from django import forms


class BoardForm(forms.Form):
    title = forms.CharField(label='제목', max_length=100)
    id = forms.CharField(label='글쓴이', max_length=50)
    content = forms.CharField(label='내용', widget=forms.Textarea)