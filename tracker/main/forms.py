from django import forms

class AddApplication(forms.Form):
    company = forms.CharField(label="company", max_length=100, required=True)
    job_title = forms.CharField(label="title", max_length=100, required=True)
    date_listed = forms.DateField(label="listed", required=False)
    date_applied = forms.DateField(label="applied", required=True)
    result = forms.CharField(label="result", max_length=20, required=False)
    contacts = forms.CharField(label="contacts", max_length=200, required=False)
    notes = forms.CharField(label="notes", max_length=300, required=False)
    link = forms.CharField(label="link", max_length=200, required=True)

class EditApplication(forms.Form):
    result = forms.CharField(label="result", max_length=20, required=False)
    notes = forms.CharField(label="notes", max_length=300, required=False)