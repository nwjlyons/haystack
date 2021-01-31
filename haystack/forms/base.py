from django import forms


class BaseForm(forms.Form):
    use_required_attribute = False


