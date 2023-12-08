{"filter":false,"title":"views.py","tooltip":"/mybugtrackproject/bugtracker/views.py","undoManager":{"mark":45,"position":45,"stack":[[{"start":{"row":0,"column":0},"end":{"row":26,"column":26},"action":"remove","lines":["from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView","from .models import Bug","","class BugListView(ListView):","    model = Bug","    template_name = 'bug_list.html'","","class BugDetailView(DetailView):","    model = Bug","    template_name = 'bug_detail.html'","","class BugCreateView(CreateView):","    model = Bug","    fields = ['title', 'description', 'status', 'project']","    template_name = 'bug_form.html'","    success_url = '/bugs/'","","class BugUpdateView(UpdateView):","    model = Bug","    fields = ['title', 'description', 'status', 'project']","    template_name = 'bug_update.html'","    success_url = '/bugs/'","","class BugDeleteView(DeleteView):","    model = Bug","    template_name = 'bug_confirm_delete.html'","    success_url = '/bugs/'"],"id":2},{"start":{"row":0,"column":0},"end":{"row":60,"column":0},"action":"insert","lines":["from django.shortcuts import render, redirect","from django.contrib import messages","from .forms import BugUpdateForm, SignUpForm","from .models import Bug","from django.contrib.auth import login, authenticate","from django.contrib.auth.decorators import login_required","","# Add your additional imports if necessary","","@login_required(login_url='/login/')","def list_bugs(request):","    title = 'List of Bugs'","    queryset = Bug.objects.filter(reported_by=request.user)  # Show bugs reported by logged-in user","    context = {\"title\": title, \"queryset\": queryset}","    return render(request, \"list_bugs.html\", context)  # Update with your template name","","@login_required(login_url='/login/')","def add_bug(request):","    if request.method == 'POST':","        form = BugUpdateForm(request.POST)","        if form.is_valid():","            bug = form.save(commit=False)","            bug.reported_by = request.user  # Associate bug with logged-in user","            bug.save()","            messages.success(request, 'Bug successfully reported')","            return redirect('/list_bugs')","    else:","        form = BugUpdateForm()","","    context = {\"form\": form, \"title\": \"Report a Bug\"}","    return render(request, \"add_bug.html\", context)  # Update with your template name","","@login_required(login_url='/login/')","def update_bug(request, pk):","    queryset = Bug.objects.get(id=pk, reported_by=request.user)  # Ensure user reported the bug","    if request.method == 'POST':","        form = BugUpdateForm(request.POST, instance=queryset)","        if form.is_valid():","            form.save()","            messages.success(request, 'Bug successfully updated')","            return redirect('/list_bugs')","    else:","        form = BugUpdateForm(instance=queryset)","","    context = {'form': form, 'title': 'Update Bug'}","    return render(request, 'add_bug.html', context)  # Update with your template name","","@login_required(login_url='/login/')","def delete_bug(request, pk):","    queryset = Bug.objects.get(id=pk, reported_by=request.user)  # Ensure user reported the bug","    if request.method == 'POST':","        bug_title = queryset.title  # Get the title of the bug","        queryset.delete()","        messages.success(request, f'Successfully deleted \"{bug_title}\"')","        return redirect('/list_bugs')","","    context = {\"title\": \"Are you sure you want to delete this bug?\", \"bug_title\": queryset.title}","    return render(request, 'delete_bug.html', context)  # Update with your template name","","# Rest of your views (signup, login_view, home, etc.) remain the same",""]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":42},"action":"remove","lines":["# Add your additional imports if necessary"],"id":3},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":61,"column":48},"action":"insert","lines":["from django.shortcuts import render, redirect","from django.contrib import messages","import boto3","from django.utils import timezone","from .forms import CropUpdateForm","from .models import Crop","from django.contrib.auth import login, authenticate","from django.shortcuts import render, redirect","from .forms import SignUpForm","from django.contrib import messages","from django.utils import timezone","from .models import Crop","from django.contrib.auth.decorators import login_required","","# Add your additional imports if necessary","from django.contrib.auth.decorators import login_required","","LOGIN_REDIRECT_URL = '/login'","","","def signup(request):","    if request.method == 'POST':","        form = SignUpForm(request.POST)","        if form.is_valid():","            form.save()","            username = form.cleaned_data.get('username')","            raw_password = form.cleaned_data.get('password1')","            user = authenticate(username=username, password=raw_password)","            login(request, user)","            return redirect('login')  # Redirect to home page or other appropriate page","    else:","        form = SignUpForm()","    return render(request, 'signup.html', {'form': form})","","def login_view(request):","    if request.method == 'POST':","        username = request.POST.get('username')","        password = request.POST.get('password')","        user = authenticate(request, username=username, password=password)","        ","        if user is not None:","            login(request, user)","            # Redirect to a success page.","            return redirect('home')  # Replace 'home' with the name of the view you want to redirect to","        else:","            # Return an 'invalid login' error message.","            messages.error(request, \"Invalid username or password.\")","","    return render(request, 'home.html')  # Assuming your login template is named 'login.html'","","","@login_required(login_url='/login/')","def home(request):","    title = 'Welcome....!!!'","    context = {\"title\": title}","    return render(request, \"home.html\", context)"],"id":4}],[{"start":{"row":61,"column":48},"end":{"row":62,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":62,"column":0},"end":{"row":62,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":24},"action":"remove","lines":["from .forms import CropUpdateForm","from .models import Crop"],"id":6},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":51},"action":"remove","lines":["from django.contrib.auth import login, authenticate"],"id":7},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":15,"column":0},"end":{"row":18,"column":57},"action":"remove","lines":["from django.contrib.auth.decorators import login_required","","# Add your additional imports if necessary","from django.contrib.auth.decorators import login_required"],"id":8}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["from .models import Crop",""],"id":9}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":12},"action":"remove","lines":["import boto3"],"id":10},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":29},"action":"remove","lines":["from .forms import SignUpForm"],"id":11},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":33},"action":"remove","lines":["from django.contrib import messages","from django.utils import timezone"],"id":12},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":45},"action":"remove","lines":["from django.shortcuts import render, redirect"],"id":13},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"remove","lines":["",""],"id":14}],[{"start":{"row":44,"column":0},"end":{"row":48,"column":48},"action":"remove","lines":["@login_required(login_url='/login/')","def home(request):","    title = 'Welcome....!!!'","    context = {\"title\": title}","    return render(request, \"home.html\", context)"],"id":15},{"start":{"row":44,"column":0},"end":{"row":49,"column":0},"action":"insert","lines":["@login_required(login_url='/login/')","def home(request):","    title = 'Welcome to Bug Tracker'","    context = {\"title\": title}","    return render(request, \"home.html\", context)",""]}],[{"start":{"row":49,"column":0},"end":{"row":50,"column":4},"action":"remove","lines":["","    "],"id":16}],[{"start":{"row":51,"column":0},"end":{"row":56,"column":87},"action":"remove","lines":["@login_required(login_url='/login/')","def list_bugs(request):","    title = 'List of Bugs'","    queryset = Bug.objects.filter(reported_by=request.user)  # Show bugs reported by logged-in user","    context = {\"title\": title, \"queryset\": queryset}","    return render(request, \"list_bugs.html\", context)  # Update with your template name"],"id":17}],[{"start":{"row":51,"column":0},"end":{"row":61,"column":0},"action":"insert","lines":["from django.shortcuts import render","from django.contrib.auth.decorators import login_required","from .models import Bug","","@login_required(login_url='/login/')","def list_bugs(request):","    title = 'List of Bugs'","    queryset = Bug.objects.filter(reported_by=request.user)  # Show bugs reported by logged-in user","    context = {\"title\": title, \"queryset\": queryset}","    return render(request, \"list_bugs.html\", context)",""],"id":18}],[{"start":{"row":51,"column":0},"end":{"row":53,"column":23},"action":"remove","lines":["from django.shortcuts import render","from django.contrib.auth.decorators import login_required","from .models import Bug"],"id":19}],[{"start":{"row":9,"column":0},"end":{"row":11,"column":23},"action":"insert","lines":["from django.shortcuts import render","from django.contrib.auth.decorators import login_required","from .models import Bug"],"id":20}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":57},"action":"remove","lines":["from django.contrib.auth.decorators import login_required"],"id":21},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":35},"action":"remove","lines":["from django.shortcuts import render"],"id":22},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":35},"action":"remove","lines":["from django.contrib import messages"],"id":23},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":23},"action":"remove","lines":["from .models import Bug"],"id":24},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":59,"column":0},"end":{"row":73,"column":85},"action":"remove","lines":["@login_required(login_url='/login/')","def add_bug(request):","    if request.method == 'POST':","        form = BugUpdateForm(request.POST)","        if form.is_valid():","            bug = form.save(commit=False)","            bug.reported_by = request.user  # Associate bug with logged-in user","            bug.save()","            messages.success(request, 'Bug successfully reported')","            return redirect('/list_bugs')","    else:","        form = BugUpdateForm()","","    context = {\"form\": form, \"title\": \"Report a Bug\"}","    return render(request, \"add_bug.html\", context)  # Update with your template name"],"id":25},{"start":{"row":59,"column":0},"end":{"row":79,"column":0},"action":"insert","lines":["from django.shortcuts import render, redirect","from django.contrib import messages","from .forms import BugUpdateForm","from django.contrib.auth.decorators import login_required","","@login_required(login_url='/login/')","def add_bug(request):","    if request.method == 'POST':","        form = BugUpdateForm(request.POST)","        if form.is_valid():","            bug = form.save(commit=False)","            bug.reported_by = request.user  # Associate bug with logged-in user","            bug.save()","            messages.success(request, 'Bug successfully reported')","            return redirect('list_bugs')","    else:","        form = BugUpdateForm()","","    context = {\"form\": form, \"title\": \"Report a Bug\"}","    return render(request, \"add_bug.html\", context)",""]}],[{"start":{"row":59,"column":0},"end":{"row":62,"column":57},"action":"remove","lines":["from django.shortcuts import render, redirect","from django.contrib import messages","from .forms import BugUpdateForm","from django.contrib.auth.decorators import login_required"],"id":26}],[{"start":{"row":7,"column":23},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":27}],[{"start":{"row":8,"column":0},"end":{"row":11,"column":57},"action":"insert","lines":["from django.shortcuts import render, redirect","from django.contrib import messages","from .forms import BugUpdateForm","from django.contrib.auth.decorators import login_required"],"id":28}],[{"start":{"row":8,"column":0},"end":{"row":11,"column":57},"action":"remove","lines":["from django.shortcuts import render, redirect","from django.contrib import messages","from .forms import BugUpdateForm","from django.contrib.auth.decorators import login_required"],"id":29}],[{"start":{"row":50,"column":0},"end":{"row":51,"column":0},"action":"remove","lines":["",""],"id":30},{"start":{"row":50,"column":0},"end":{"row":51,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":56,"column":0},"end":{"row":57,"column":0},"action":"remove","lines":["",""],"id":31},{"start":{"row":56,"column":0},"end":{"row":57,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":61,"column":42},"end":{"row":62,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":62,"column":0},"end":{"row":62,"column":8},"action":"insert","lines":["        "]},{"start":{"row":62,"column":8},"end":{"row":62,"column":9},"action":"insert","lines":["p"]},{"start":{"row":62,"column":9},"end":{"row":62,"column":10},"action":"insert","lines":["r"]},{"start":{"row":62,"column":10},"end":{"row":62,"column":11},"action":"insert","lines":["i"]},{"start":{"row":62,"column":11},"end":{"row":62,"column":12},"action":"insert","lines":["n"]},{"start":{"row":62,"column":12},"end":{"row":62,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":62,"column":13},"end":{"row":62,"column":15},"action":"insert","lines":["()"],"id":33}],[{"start":{"row":62,"column":14},"end":{"row":62,"column":16},"action":"insert","lines":["\"\""],"id":34}],[{"start":{"row":62,"column":15},"end":{"row":62,"column":16},"action":"insert","lines":["p"],"id":35},{"start":{"row":62,"column":16},"end":{"row":62,"column":17},"action":"insert","lines":["o"]},{"start":{"row":62,"column":17},"end":{"row":62,"column":18},"action":"insert","lines":["s"]},{"start":{"row":62,"column":18},"end":{"row":62,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":63,"column":27},"end":{"row":64,"column":0},"action":"insert","lines":["",""],"id":36},{"start":{"row":64,"column":0},"end":{"row":64,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":64,"column":12},"end":{"row":64,"column":25},"action":"insert","lines":["print(\"post\")"],"id":37}],[{"start":{"row":64,"column":23},"end":{"row":64,"column":24},"action":"insert","lines":[" "],"id":38},{"start":{"row":64,"column":24},"end":{"row":64,"column":25},"action":"insert","lines":["v"]},{"start":{"row":64,"column":25},"end":{"row":64,"column":26},"action":"insert","lines":["a"]},{"start":{"row":64,"column":26},"end":{"row":64,"column":27},"action":"insert","lines":["l"]},{"start":{"row":64,"column":27},"end":{"row":64,"column":28},"action":"insert","lines":["i"]},{"start":{"row":64,"column":28},"end":{"row":64,"column":29},"action":"insert","lines":["d"]}],[{"start":{"row":85,"column":30},"end":{"row":85,"column":39},"action":"remove","lines":["list_bugs"],"id":39},{"start":{"row":85,"column":30},"end":{"row":85,"column":40},"action":"insert","lines":["bugs/list/"]}],[{"start":{"row":99,"column":25},"end":{"row":99,"column":35},"action":"remove","lines":["/list_bugs"],"id":40},{"start":{"row":99,"column":25},"end":{"row":99,"column":36},"action":"insert","lines":["/bugs/list/"]}],[{"start":{"row":35,"column":29},"end":{"row":35,"column":33},"action":"remove","lines":["home"],"id":41},{"start":{"row":35,"column":29},"end":{"row":35,"column":30},"action":"insert","lines":["/"]}],[{"start":{"row":10,"column":29},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":42}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":24},"action":"insert","lines":["LOGIN_REDIRECT_URL = '/'"],"id":43}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":29},"action":"remove","lines":["LOGIN_REDIRECT_URL = '/login'"],"id":44}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["",""],"id":45},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":24},"action":"remove","lines":["LOGIN_REDIRECT_URL = '/'"],"id":46}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["",""],"id":47},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":1181.4000000000005,"scrollleft":0,"selection":{"start":{"row":8,"column":0},"end":{"row":8,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":83,"state":"start","mode":"ace/mode/python"}},"timestamp":1702050249972,"hash":"50f91b396e4d0b3da939a7afb25b33cad609ea75"}