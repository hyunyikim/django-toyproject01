from django import forms


class BoardForm(forms.Form):
    num = forms.CharField(label='글번호')
    title = forms.CharField(label='제목', max_length=100)
    id = forms.CharField(label='글쓴이', max_length=50)
    content = forms.CharField(label='내용', widget=forms.Textarea)