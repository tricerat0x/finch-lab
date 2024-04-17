from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Feeding
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    
    if request.method == 'POST':
        form = FeedingForm(request.POST)
        if form.is_valid():
            new_feeding = form.save(commit=False)
            new_feeding.finch = finch
            new_feeding.save()
            return redirect('finches_detail', finch_id=finch.id)
    
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form,
    })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

    def get_success_url(self):
        return reverse('finches_detail', kwargs={'finch_id': self.object.id})

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('finches_detail', kwargs={'finch_id': self.object.id})

class FinchDelete(DeleteView):
    model = Finch

    def get_success_url(self):
        return reverse('finches_index')

