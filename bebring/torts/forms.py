from django import forms
from .models import Offer, Tort, StatusForOffer, Problem


class OfferForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Ваше имя')
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label="Ваш телефон")
    description = forms.CharField(widget=forms.Textarea, label="Комментарий к заказу", max_length=10000)
    tort = forms.ModelChoiceField(queryset=Tort.objects.all(), label="Торт")
    # status = forms.ModelChoiceField(queryset=StatusForOffer.objects.all())

    # def __init__(self, *args, **kwargs):
    #     super(OfferForm, self).__init__(*args, **kwargs)
    #     self.fields['tort'] = forms.ChoiceField(
    #         choices=[(o.id, o) for o in Tort.objects.all()], label="Торт"
    #     )

    class Meta:
        model = Offer
        fields = ['name', 'phone_number', 'description', 'tort']


class ProblemForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Ваше имя')
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label="Ваш телефон")
    description = forms.CharField(widget=forms.Textarea, label="Комментарий к заказу", max_length=10000)
    tort = forms.ModelChoiceField(queryset=Tort.objects.all(), label="Торт")
    problem_photo = forms.ImageField(label='Фото проблемы')

    class Meta:
        model = Problem
        fields = ['name', 'phone_number', 'description', 'tort', 'problem_photo']