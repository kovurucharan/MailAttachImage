from django import forms

class MailAttachForm(forms.Form):
    Name=forms.CharField(max_length=30)
    Email=forms.CharField(max_length=30)
    Subject=forms.CharField(max_length=100)
    Message=forms.CharField(required=False)
    Imgatta=forms.FileField(required=False)