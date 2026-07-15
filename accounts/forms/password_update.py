from django import forms
from django.contrib.auth import password_validation


class PasswordUpdateForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(), label='Old password')
    new_password = forms.CharField(widget=forms.PasswordInput(), label='New password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm new password')

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if self.user and not self.user.check_password(old_password):
            raise forms.ValidationError('Current password is incorrect')
        return old_password

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        if new_password:
            password_validation.validate_password(new_password, self.user)
        return new_password

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError('The new password and its repetition do not match')

        if old_password and new_password and old_password == new_password:
            raise forms.ValidationError('New password must not match the old password')

        return cleaned_data
