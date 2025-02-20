# views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def feedback_view(request):
    if request.method == 'POST':
        print(request.POST) 
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def feedback_success(request):
    return render(request, 'feedback_success.html')
