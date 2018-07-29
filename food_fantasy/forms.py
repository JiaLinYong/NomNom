from django import forms

class IngredientForm(forms.Form):
    your_ingredients = forms.CharField(label='Your ingredients', max_length=100)

        