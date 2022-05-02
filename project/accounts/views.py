from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from home_app.models import Profile
# Create your views here.
def sinup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('app:all_boys')
    return render(request, 'accounts/sinup.html',{'form':form})
def profile(request):
    profile = profile.object.get(user=request.user)
    return render(request,'profile.html',context={'profile':profile})