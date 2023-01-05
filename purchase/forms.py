from django import forms
from .models import Payment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'autocomplete': 'off'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'required': 'true'}),

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'name',
            'amount',
            Submit('submit', 'Buy', css_class='button white btn-block btn-primary')
        )
