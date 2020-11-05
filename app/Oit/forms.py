from django import forms  
from Oit.models import Model_OIT  

class Model_OIT_Form(forms.ModelForm): 

    class Meta:  
        model = Model_OIT  
        fields = "__all__"  