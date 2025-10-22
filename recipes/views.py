from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'global/index.html', context={
        'name': 'global templates page',
    })
