from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })

finches = [
  {'name': 'Lolo', 'type': 'Zebra Finch', 'description': 'small birds with strips', 'age': 3},
  {'name': 'Sachi', 'type': 'American Goldfinch', 'description': 'bright yellow and black plumage', 'age': 2},
]