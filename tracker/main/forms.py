from django.forms import Form, ModelForm, CharField, DateField
from .models import Application


class AddApplication(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'

class EditApplication(ModelForm):
    class Meta:
        model = Application
        fields = ['notes', 'result']

# class AddApplication(Form):
#     company = CharField(label="company", max_length=100, required=True)
#     job_title = CharField(label="title", max_length=100, required=True)
#     date_listed = DateField(label="listed", required=False)
#     date_applied = DateField(label="applied", required=True)
#     result = CharField(label="result", max_length=20, required=False)
#     contacts = CharField(label="contacts", max_length=200, required=False)
#     notes = CharField(label="notes", max_length=300, required=False)
#     link = CharField(label="link", max_length=200, required=True)

# class EditApplication(Form):
#     result = CharField(label="result", max_length=20, required=False)
#     notes = CharField(label="notes", max_length=300, required=False)