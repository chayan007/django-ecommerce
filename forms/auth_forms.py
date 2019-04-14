from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter the Username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter the Password"
            }
        )
    )


class RegisterForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter the Name"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter the Name"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter the Username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter the Password"
            }
        )
    )
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter the Password Again"
            }
        )
    )
