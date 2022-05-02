from django import forms
from .models import boy,classes,techers,absence,Transport,driver,masrof, darajat, mawad
# from .views import classssss
# def classs(request):
#     return classes.objects.filter(user=request.user)
class boy_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # boy_class = forms.ModelChoiceField()
    class Meta:
        model = boy
        fields = '__all__'
        exclude = ('user',)

class class_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = classes
        fields = '__all__'
        exclude = ('user',)
class techer_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = techers
        fields = '__all__'
        exclude = ('user',)

class absence_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = absence
        fields = '__all__'
        exclude = ('user',)

class Transport_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Transport
        fields = '__all__'
        exclude = ('user',)

class driver_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = driver
        fields = '__all__'
        exclude = ('user',)

class masrof_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = masrof
        fields = '__all__'
        exclude = ('user',)

class darajat_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = darajat
        fields = '__all__'
        exclude = ('user','profile')

class mawad_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = mawad
        fields = '__all__'
        exclude = ('user',)

class absence_search(forms.Form):
    serchname = forms.CharField(widget=forms.TextInput())
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # print('kgkgkgk____________________________________+++++++++++++++++++++')