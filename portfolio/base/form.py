from. models import Message
from django import forms
from django.core.exceptions import ValidationError




class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone_no', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Phone Number (required)' }),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 4}),
        }

        error_messages = {
            'phone_number': {
                'required': 'Phone Number Required '
            }
        }


        def clean_phone_number(self):
            phone_no = self.cleaned_data.get('phone_no')
            if not phone_no:
                raise ValidationError('Phone Number is Required')
            
            return phone_no
