from django import forms

class ArticleForm(forms.Form):
    # 나머지는 자동으로 만들어주니까 안 받아도 됨
    title = forms.CharField(
        max_length=20,
        label = 'name',
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label = 'story',
        widget = forms.Textarea(
            attrs={
                'placeholder': 'Under the See',
                'rows': 5,
                'cols': 50,
            }
        )
    )
    

class StudentForm(foms.Form):
    name = forms.CharField(max_legth=20)
    age = forms.IntegerField()
    