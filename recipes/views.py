from django.shortcuts import render

# Create your views here.
def index(reques):
    return render(reques, 'recipes/index.html', context={
        'name': 'Lucas Teixeira'
    })