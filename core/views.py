from django.shortcuts import render, redirect
from .models import uploader
from .forms import uploaderform
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = uploaderform()
        candidates = uploader.objects.all()
        
        context = {
            'form':form,
            'candidates': candidates
        }
        return render(request, 'home.html', context)
    def post(self, request):
        form = uploaderform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        candidates = uploader.objects.all() 
        context = {
            'form':form,
            'candidates': candidates
        }        
        return render(request, 'home.html', context)


class ProfileView(View):
    def get(self, request,pk):
        candidate = uploader.objects.get(pk=pk)
        context = {
            'candidate' : candidate
        }
        return render(request, 'profile.html', context)