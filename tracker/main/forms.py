from django import forms

class AddApplication(forms.Form):
    company = forms.CharField(label="company", max_length=100)
    job_title = forms.CharField(label="title", max_length=100)
    date_listed = forms.DateField(label="listed", required=False)
    date_applied = forms.DateField(label="applied", required=True)
    follow_up = forms.BooleanField(label="follow-up")
    result = forms.CharField(label="result", max_length=20)
    contacts = forms.CharField(label="contacts", max_length=200)
    notes = forms.CharField(label="notes", max_length=300)