from django import forms

class ContactForm(forms.Form):
    nama        = forms.CharField(
                    max_length  = 50,
                    label       = "Name",
                    widget      = forms.TextInput(
                        attrs   = {
                            'class':'form-control',
                            'placeholder':'Vollständiger Name'
                            }
                        )
                    )

    jenkel      = (
                    ('L', 'Männlich'),('P','Weiblich'),
                    )

    gender      = forms.ChoiceField(
                    widget      = forms.RadioSelect(
                        attrs   = {
                            'class':'form-check-input'
                            }
                        ),
                    choices     = jenkel,
                    label       = "Geschlecht"
                    )

    TAHUN       = range(1960,2020,1)

    dateofbirth = forms.DateField(
                    widget      = forms.SelectDateWidget(
                        attrs   = {
                            'class':'form-control col-sm-2',
                            },
                        years   = TAHUN
                        ),
                    label       = "Geburtsdatum"
                    )
                
    alamat      = forms.CharField(
                    widget      = forms.Textarea(
                        attrs   = {
                            'class':'form-control',
                            'placeholder':'Deine Adresse'
                        }
                    ),
                    max_length  = 100,
                    required    = False,
                    label       = "Adresse"
                    )

    agree       = forms.BooleanField(
                    widget      = forms.CheckboxInput(
                        attrs   = {
                            'class':'form-check-input',
                        }
                    ),
                    label       = "Zustimmen"
                    )