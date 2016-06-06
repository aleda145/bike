from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions, StrictButton)

class ContactForm(forms.Form):
    name = forms.CharField(required=True,
                           label = "Name",
                            )
    email = forms.EmailField(required=True,
                             label = "Email",
                             )
    subject = forms.CharField(required=True,
                              label = "Subject",
                              )
    message = forms.CharField(required=True,
                              widget=forms.Textarea,
                              label = "Message",)


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-contactform'
        self.helper.form_class = 'contactform'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'name',
            'email',
            'subject',
            'message',
)