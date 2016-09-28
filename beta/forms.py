from django import forms
from beta.models import *
from beta.choices import *
from functools import partial


class SignupForm(forms.Form):
    first_name =        forms.CharField(max_length=30, label='First Name')
    last_name =         forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        
class TesterForm(forms.ModelForm):
    region =            forms.ChoiceField(choices=REGIONS)
    country =           forms.ChoiceField(choices=AFRICAN_COUNTRIES)
    city =              forms.CharField()
    age =               forms.IntegerField()
    sex =               forms.ChoiceField(choices=GENDER)
    social_account =    forms.URLField()
    industry =          forms.ChoiceField(choices=INDUSTRY)
    
    class Meta:
        model = Tester
        fields = ('region', 'country', 'city', 'age', 'sex', 'social_account',
                  'industry',)

class StartupForm(forms.ModelForm):
    startup =           forms.CharField(label="Startup Name")
    tagline =           forms.CharField()
    home_page =         forms.ImageField()
    logo =              forms.ImageField(required=False, widget=forms.FileInput(attrs={'placeholder':'Optional'}))
    category =          forms.ChoiceField(choices=CAT)
    #status =            forms.ChoiceField(choices=BETA_STATUS)
    stat =              forms.ChoiceField(choices=STATUS, label="Status")
    description =       forms.CharField(widget=forms.Textarea)
    country =           forms.ChoiceField(choices=AFRICAN_COUNTRIES)
    city =              forms.CharField()
    url =               forms.URLField(widget=forms.URLInput(attrs={'placeholder':'http://www.mywebsite.com'}))
    
    class Meta:
        model = Startup
        fields = ('startup', 'tagline',  'home_page', 'logo',
                  'category', 'stat', 'description', 'country', 'city',
                  'url')
        
class BetaTestForm(forms.ModelForm):
    name =              forms.CharField()
    tagline =           forms.CharField()
    description =       forms.CharField(widget=forms.Textarea)
    logo =              forms.ImageField(required=False)
    link =              forms.URLField(required=False)
    app_file =          forms.FileField(required=False)
    region =            forms.ChoiceField(choices=REGIONS)
    country =           forms.ChoiceField(choices=AFRICAN_COUNTRIES)
    city =              forms.CharField()
    age_from =          forms.CharField()
    age_to =            forms.CharField()
    sex =               forms.ChoiceField(choices=TARGETED_GENDER, label="Targeted gender")
    start_date =        forms.DateField(widget=forms.DateInput)
    end_date =          forms.DateField(widget=forms.DateInput)
    
    class Meta:
        model = BetaTest
        fields = ('name', 'tagline', 'description', 'logo', 'link', 'app_file',
                  'region', 'country', 'city', 'age_from', 'age_to', 'sex',
                  'start_date', 'end_date',)
        
class TeamForm(forms.ModelForm):
    full_name =         forms.CharField()
    photo =             forms.ImageField()
    twitter_handle =    forms.CharField()
    role =              forms.ChoiceField(choices=TEAM_ROLE)
    
    class Meta:
        model = Team
        fields = ('full_name', 'photo', 'twitter_handle', 'role', )
        
class SignUpForm(forms.ModelForm):
    first_name =        forms.CharField()
    last_name =         forms.CharField()
    email =             forms.EmailField()
    phone_number =      forms.CharField(required=False)
    
    class Meta:
        model = SignUp
        fields = ('first_name', 'last_name', 'email', 'phone_number')

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
      
class SubmitStartupForm(forms.ModelForm):
    startup =           forms.CharField()
    tagline =           forms.CharField()
    home_page =         forms.ImageField()
    logo =              forms.ImageField(required=False)
    #launching =         forms.DateField(required=False)
    category =          forms.ChoiceField(choices=CAT)
    description =       forms.CharField(widget=forms.Textarea)
    #region =            forms.ChoiceField(choices=REGIONS)
    country =           forms.ChoiceField(choices=AFRICAN_COUNTRIES)
    city =              forms.CharField()
    url =               forms.URLField()
    #tag =               forms.ChoiceField(choices=RELATED_TAGS)
    promoted =          forms.BooleanField(required=False)
    status =            forms.ChoiceField(choices=BETA_STATUS)
    pub_status =        forms.ChoiceField(choices=PUB_STATUS)
    #published =         forms.BooleanField(required=False)
    pub_date =          forms.DateField(required=False)
    
    class Meta:
        model = Startup
        fields = ('startup', 'tagline', 'home_page', 'logo', 'category',
                  'description','country', 'city', 'url', 'promoted',
                 'status', 'pub_status', 'pub_date')
        
class Contact_UsForm(forms.Form):
    name = forms.CharField(label="Full Name")
    email = forms.EmailField(required=False)
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 50,}), required=False)
    #captcha = NoReCaptchaField()
    
class NewsletterForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = NewLetter
        fields = ('email', )
    
    
