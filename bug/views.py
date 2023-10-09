from django.shortcuts import render, redirect, get_object_or_404
from .models import Bug
from .forms import BugForm

def register_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_list')
    else:
        form = BugForm()
    return render(request, 'register_bug.html', {'form': form})

def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'bug_list.html', {'bugs': bugs})

def bug_detail(request, bug_id):
    bug = get_object_or_404(Bug, id=bug_id)
    return render(request, 'bug_detail.html', {'bug': bug})