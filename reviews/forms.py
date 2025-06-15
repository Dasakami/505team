from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Row, Column, HTML
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'company', 'avatar', 'rating', 'title', 'text', 'service_used', 'would_recommend']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'company': forms.TextInput(attrs={'placeholder': 'Название компании (необязательно)'}),
            'title': forms.TextInput(attrs={'placeholder': 'Заголовок отзыва'}),
            'text': forms.Textarea(attrs={'placeholder': 'Расскажите о вашем опыте работы с нами...', 'rows': 5}),
            'service_used': forms.TextInput(attrs={'placeholder': 'Какую услугу вы заказывали?'}),
            'rating': forms.Select(choices=[(i, f'{i} звезд{"а" if i in [2,3,4] else ""}') for i in range(1, 6)]),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'
        self.helper.layout = Layout(
            HTML('<h3 class="text-xl font-bold mb-4">Оставить отзыв</h3>'),
            Row(
                Column('name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('company', css_class='form-group col-md-6 mb-3'),
                Column('rating', css_class='form-group col-md-6 mb-3'),
            ),
            Field('title', css_class='form-group mb-3'),
            Field('text', css_class='form-group mb-3'),
            Row(
                Column('service_used', css_class='form-group col-md-8 mb-3'),
                Column('would_recommend', css_class='form-group col-md-4 mb-3'),
            ),
            Field('avatar', css_class='form-group mb-3'),
            Submit('submit', 'Отправить отзыв', css_class='btn btn-primary w-full')
        )