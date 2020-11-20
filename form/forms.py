from django import forms
from django.core.exceptions import ValidationError

from .models import InfoModel

class InfoForm(forms.ModelForm):
    class Meta:
        model = InfoModel
        fields = ['first_name','last_name','email','phone','selection',
            'type0','type1', 'type2']
        labels = {'first_name':'الاسم الأول','last_name':'الاسم العائلي', 'email':'البريد الالكتروني',
        'phone':'رقم الهاتف', 'selection':'الاختيار', }
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        
        if not phone.isnumeric():
            # phone contains other than numbers
            raise ValidationError("Please enter numbers only.")
        elif len(phone) != 10:
            raise ValidationError("Enter a 10 digits number.")
        
        return phone
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        if not first_name.isalpha():
            # name contains other than alphabetic characters
            raise ValidationError("Enter only alphabetic characters حمزة")

        return first_name 