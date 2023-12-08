{"filter":false,"title":"forms.py","tooltip":"/mybugtrackproject/bugtracker/forms.py","undoManager":{"mark":27,"position":27,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["from django import forms","from .models import Bug","","class BugUpdateForm(forms.ModelForm):","    class Meta:","        model = Bug","        fields = ['title', 'description', 'status', 'project', 'priority']","        widgets = {","            'title': forms.TextInput(attrs={'class': 'form-control'}),","            'description': forms.Textarea(attrs={'class': 'form-control'}),","            'status': forms.Select(attrs={'class': 'form-control'}),","            'project': forms.TextInput(attrs={'class': 'form-control'}),","            'priority': forms.Select(attrs={'class': 'form-control'}, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]),","        }",""],"id":1}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":15,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["class SignUpForm(UserCreationForm):","    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')","","    class Meta:","        model = User","        fields = ('username', 'email', 'password1', 'password2', )",""],"id":3}],[{"start":{"row":1,"column":23},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":2,"column":0},"end":{"row":6,"column":43},"action":"insert","lines":["from django import forms","from .models import Crop","from django import forms","from django.contrib.auth.forms import UserCreationForm","from django.contrib.auth.models import User"],"id":5}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":24},"action":"remove","lines":["from .models import Crop"],"id":6},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":24},"action":"remove","lines":["from django import forms"],"id":7},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":66},"end":{"row":13,"column":68},"action":"remove","lines":["),"],"id":8},{"start":{"row":13,"column":66},"end":{"row":13,"column":132},"action":"insert","lines":["choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]),"]}],[{"start":{"row":13,"column":77},"end":{"row":13,"column":80},"action":"remove","lines":["Low"],"id":9},{"start":{"row":13,"column":77},"end":{"row":13,"column":78},"action":"insert","lines":["N"]},{"start":{"row":13,"column":78},"end":{"row":13,"column":79},"action":"insert","lines":["e"]},{"start":{"row":13,"column":79},"end":{"row":13,"column":80},"action":"insert","lines":["w"]}],[{"start":{"row":13,"column":86},"end":{"row":13,"column":87},"action":"remove","lines":["w"],"id":10},{"start":{"row":13,"column":85},"end":{"row":13,"column":86},"action":"remove","lines":["o"]},{"start":{"row":13,"column":84},"end":{"row":13,"column":85},"action":"remove","lines":["L"]}],[{"start":{"row":13,"column":84},"end":{"row":13,"column":85},"action":"insert","lines":["O"],"id":11},{"start":{"row":13,"column":85},"end":{"row":13,"column":86},"action":"insert","lines":["p"]},{"start":{"row":13,"column":86},"end":{"row":13,"column":87},"action":"insert","lines":["e"]},{"start":{"row":13,"column":87},"end":{"row":13,"column":88},"action":"insert","lines":["n"]}],[{"start":{"row":13,"column":94},"end":{"row":13,"column":100},"action":"remove","lines":["Medium"],"id":12},{"start":{"row":13,"column":94},"end":{"row":13,"column":95},"action":"insert","lines":["A"]},{"start":{"row":13,"column":95},"end":{"row":13,"column":96},"action":"insert","lines":["s"]},{"start":{"row":13,"column":96},"end":{"row":13,"column":97},"action":"insert","lines":["s"]},{"start":{"row":13,"column":97},"end":{"row":13,"column":98},"action":"insert","lines":["i"]},{"start":{"row":13,"column":98},"end":{"row":13,"column":99},"action":"insert","lines":["g"]},{"start":{"row":13,"column":99},"end":{"row":13,"column":100},"action":"insert","lines":["n"]},{"start":{"row":13,"column":100},"end":{"row":13,"column":101},"action":"insert","lines":["e"]},{"start":{"row":13,"column":101},"end":{"row":13,"column":102},"action":"insert","lines":["d"]}],[{"start":{"row":13,"column":106},"end":{"row":13,"column":112},"action":"remove","lines":["Medium"],"id":13},{"start":{"row":13,"column":106},"end":{"row":13,"column":107},"action":"insert","lines":["I"]},{"start":{"row":13,"column":107},"end":{"row":13,"column":108},"action":"insert","lines":["n"]},{"start":{"row":13,"column":108},"end":{"row":13,"column":109},"action":"insert","lines":["P"]},{"start":{"row":13,"column":109},"end":{"row":13,"column":110},"action":"insert","lines":["r"]},{"start":{"row":13,"column":110},"end":{"row":13,"column":111},"action":"insert","lines":["o"]},{"start":{"row":13,"column":111},"end":{"row":13,"column":112},"action":"insert","lines":["g"]},{"start":{"row":13,"column":112},"end":{"row":13,"column":113},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":113},"end":{"row":13,"column":114},"action":"insert","lines":["r"],"id":14}],[{"start":{"row":13,"column":113},"end":{"row":13,"column":114},"action":"remove","lines":["r"],"id":15}],[{"start":{"row":13,"column":113},"end":{"row":13,"column":114},"action":"insert","lines":["r"],"id":16}],[{"start":{"row":13,"column":113},"end":{"row":13,"column":114},"action":"remove","lines":["r"],"id":17},{"start":{"row":13,"column":112},"end":{"row":13,"column":113},"action":"remove","lines":["e"]}],[{"start":{"row":13,"column":112},"end":{"row":13,"column":113},"action":"insert","lines":["r"],"id":18},{"start":{"row":13,"column":113},"end":{"row":13,"column":114},"action":"insert","lines":["e"]},{"start":{"row":13,"column":114},"end":{"row":13,"column":115},"action":"insert","lines":["s"]},{"start":{"row":13,"column":115},"end":{"row":13,"column":116},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":122},"end":{"row":13,"column":126},"action":"remove","lines":["High"],"id":19},{"start":{"row":13,"column":122},"end":{"row":13,"column":123},"action":"insert","lines":["F"]},{"start":{"row":13,"column":123},"end":{"row":13,"column":124},"action":"insert","lines":["i"]},{"start":{"row":13,"column":124},"end":{"row":13,"column":125},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":125},"end":{"row":13,"column":126},"action":"insert","lines":["d"],"id":20}],[{"start":{"row":13,"column":124},"end":{"row":13,"column":125},"action":"insert","lines":["x"],"id":21}],[{"start":{"row":13,"column":131},"end":{"row":13,"column":135},"action":"remove","lines":["High"],"id":22},{"start":{"row":13,"column":131},"end":{"row":13,"column":132},"action":"insert","lines":["P"]},{"start":{"row":13,"column":132},"end":{"row":13,"column":133},"action":"insert","lines":["e"]},{"start":{"row":13,"column":133},"end":{"row":13,"column":134},"action":"insert","lines":["n"]},{"start":{"row":13,"column":134},"end":{"row":13,"column":135},"action":"insert","lines":["d"]},{"start":{"row":13,"column":135},"end":{"row":13,"column":136},"action":"insert","lines":["i"]},{"start":{"row":13,"column":136},"end":{"row":13,"column":137},"action":"insert","lines":["n"]},{"start":{"row":13,"column":137},"end":{"row":13,"column":138},"action":"insert","lines":["g"]}],[{"start":{"row":13,"column":131},"end":{"row":13,"column":138},"action":"remove","lines":["Pending"],"id":23},{"start":{"row":13,"column":131},"end":{"row":13,"column":132},"action":"insert","lines":["C"]},{"start":{"row":13,"column":132},"end":{"row":13,"column":133},"action":"insert","lines":["l"]},{"start":{"row":13,"column":133},"end":{"row":13,"column":134},"action":"insert","lines":["o"]},{"start":{"row":13,"column":134},"end":{"row":13,"column":135},"action":"insert","lines":["s"]},{"start":{"row":13,"column":135},"end":{"row":13,"column":136},"action":"insert","lines":["e"]},{"start":{"row":13,"column":136},"end":{"row":13,"column":137},"action":"insert","lines":["d"]}],[{"start":{"row":13,"column":122},"end":{"row":13,"column":127},"action":"remove","lines":["Fixed"],"id":24},{"start":{"row":13,"column":122},"end":{"row":13,"column":128},"action":"insert","lines":["Closed"]}],[{"start":{"row":13,"column":94},"end":{"row":13,"column":102},"action":"remove","lines":["Assigned"],"id":25},{"start":{"row":13,"column":94},"end":{"row":13,"column":104},"action":"insert","lines":["InProgress"]}],[{"start":{"row":13,"column":77},"end":{"row":13,"column":80},"action":"remove","lines":["New"],"id":26},{"start":{"row":13,"column":77},"end":{"row":13,"column":81},"action":"insert","lines":["Open"]}],[{"start":{"row":13,"column":66},"end":{"row":13,"column":67},"action":"insert","lines":[","],"id":27}],[{"start":{"row":13,"column":67},"end":{"row":13,"column":68},"action":"insert","lines":[" "],"id":28}]]},"ace":{"folds":[],"scrolltop":1.5000000000002922,"scrollleft":0,"selection":{"start":{"row":5,"column":0},"end":{"row":5,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1702056300592,"hash":"4949fdd4c32638b2830515247b8da74813193c7b"}