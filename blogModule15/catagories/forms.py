from django.forms import ModelForm
from .models import Catagory

class CategoryForm(ModelForm):
    class Meta:
        model = Catagory
        fields = '__all__'