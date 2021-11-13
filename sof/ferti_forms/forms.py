from django import forms

crops=['rice','maize','chickpea']

class FertilizerForm(forms.Form):
    # cropname = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=crops,
    # )
    cropname=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Crop Name (example:rice)'}))
    phosphorous=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Phosphorus value (example:50)'}))
    nitrogen=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter nitrogen value (example:50)'}))
    potassium=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Potassium value (example:50)'}))
