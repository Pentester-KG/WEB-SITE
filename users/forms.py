from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save
from . import models
from django.dispatch import receiver
from .models import UserProfile

GENDER = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )
MARRIED_STATUS = (
    ('Женат(а)', 'Женат(а)'),
    ('Не женат(а)', 'Не женат(а)')
)


# class RegisterUserForm(UserCreationForm):
#     phone_number = forms.CharField(required=True)
#     education = forms.BooleanField(required=True)
#     habits = forms.CharField(required=True)
#     exp_work = forms.IntegerField(required=True)
#     age = forms.IntegerField(required=True)
#     gender = forms.ChoiceField(choices=GENDER, required=True)
#     married_status = forms.ChoiceField(choices=MARRIED_STATUS, required=True)
#
#     class Meta:
#         model = models.UserProfile
#         fields = (
#             'username',
#             'email1',
#             'password1',
#             'password2',
#             'first_name',
#             'last_name',
#             'age',
#             'gender',
#             'phone_number',
#             'experience_work'
#         )
#
#     def save(self, commit=True):
#         user = super(RegisterUserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email1']
#         if commit:
#             user.save()
#         return user
#
class RegisterUserForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    education = forms.BooleanField(required=True)
    habits = forms.CharField(required=True)
    exp_work = forms.IntegerField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    married_status = forms.ChoiceField(choices=MARRIED_STATUS, required=True)



    class Meta:
        model = UserProfile
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number',
            'exp_work',
            'education',
            'habits',
            'married_status',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
@receiver(post_save, sender=UserProfile)
def set_experience(sender, instance, created, **kwargs):
    if created:
        print('Сигнал обработан пользователь создан')
    exp = instance.exp
    if exp <= 1:
        instance.experience_work = 'Junior'
    elif 1 <= exp <= 3:
        instance.experience_work = 'Middle'
    elif 3 <= exp <= 25:
        instance.experience_work = 'Senior'
    else:
        instance.experience_work = "Стаж не определен"
    instance.save()



