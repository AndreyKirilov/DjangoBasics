from django import forms
from Fruitipedia_app.fruits.models import Fruit


class CreateFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description', 'nutrition']
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'})
        }


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description', 'nutrition']
        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
            'nutrition': 'Nutrition:'
        }


class DeleteFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description']
        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:'
        }

    def __init__(self, *args, **kwargs):
        super(DeleteFruitForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
