from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BugUpdateForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Bug

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')  # Redirect to home page or other appropriate page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')  # Replace 'home' with the name of the view you want to redirect to
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Invalid username or password.")

    return render(request, 'home.html')  # Assuming your login template is named 'login.html'


@login_required(login_url='/login/')
def home(request):
    title = 'Welcome to Bug Tracker'
    context = {"title": title}
    return render(request, "home.html", context)


@login_required(login_url='/login/')
def list_bugs(request):
    title = 'List of Bugs'
    queryset = Bug.objects.filter(reported_by=request.user)  # Show bugs reported by logged-in user
    context = {"title": title, "queryset": queryset}
    return render(request, "list_bugs.html", context)


@login_required(login_url='/login/')
def add_bug(request):
    if request.method == 'POST':
        form = BugUpdateForm(request.POST)
        print("post")
        if form.is_valid():
            print("post valid")
            bug = form.save(commit=False)
            bug.reported_by = request.user  # Associate bug with logged-in user
            bug.save()
            messages.success(request, 'Bug successfully reported')
            return redirect('list_bugs')
    else:
        form = BugUpdateForm()

    context = {"form": form, "title": "Report a Bug"}
    return render(request, "add_bug.html", context)


@login_required(login_url='/login/')
def update_bug(request, pk):
    queryset = Bug.objects.get(id=pk, reported_by=request.user)  # Ensure user reported the bug
    if request.method == 'POST':
        form = BugUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bug successfully updated')
            return redirect('/bugs/list/')
    else:
        form = BugUpdateForm(instance=queryset)

    context = {'form': form, 'title': 'Update Bug'}
    return render(request, 'add_bug.html', context)  # Update with your template name

@login_required(login_url='/login/')
def delete_bug(request, pk):
    queryset = Bug.objects.get(id=pk, reported_by=request.user)  # Ensure user reported the bug
    if request.method == 'POST':
        bug_title = queryset.title  # Get the title of the bug
        queryset.delete()
        messages.success(request, f'Successfully deleted "{bug_title}"')
        return redirect('/bugs/list/')

    context = {"title": "Are you sure you want to delete this bug?", "bug_title": queryset.title}
    return render(request, 'delete_bug.html', context)  # Update with your template name

# Rest of your views (signup, login_view, home, etc.) remain the same
