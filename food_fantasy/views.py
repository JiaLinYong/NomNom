from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .forms import IngredientForm
import requests
import json

def index(request):
    return HttpResponse("Hello, welcome to my page!")


def return_recipe(request):
    form = IngredientForm()
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredients = form.cleaned_data["your_ingredients"]
            recipes = get_recipe(ingredients)
            # TODO: remove me     
            recipe1 = Recipe("foo", "bar", "baz")
            recipe2 = Recipe("foo", "bar", "baz")
            recipe3 = Recipe("foo", "bar", "baz")
            recipes = [recipe1, recipe2, recipe3]
            # Rendering the page with the recipes 
            
            return HttpResponse(recipes[2].label)
    return render(request, 'form.html', { 'form': form })


class Recipe:
    label = ""
    image = ""
    url = ""
    def __init__(self, label, image, url):
        self.label = label
        self.image = image
        self.url = url

def get_recipe(ingredients):
    url = "https://api.edamam.com/search?q=" + ingredients + "&app_id=12f2a621&app_key=3c2257e872a964e2af1a5636c38bd9b1&from=0&to=3&calories=591-722&health=alcohol-free&ingredients=pork"
    response = requests.get(url)
    if response.status_code == 200:
        response_hits = json.loads(response.text)['hits']
        recipe_list = []
        for hit in response_hits:
            recipe = hit['recipe']
            label = recipe['label']
            image = recipe['image']
            url = recipe['url']
            r = Recipe(label,image,url)
            recipe_list.append(r)
        return recipe_list
    else:
        return response.status_code
            





        

        


