from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import boy,classes,techers,absence,Transport,driver,masrof,Profile,darajat,mawad
from django.core.paginator import Paginator
from .filters import BoyFilter, mawadFilter, techersFilter, absenceFilter, masrofFilter, classFilter,driverFilter, darajatFilter,Transport_Filter
from django.contrib.auth.decorators import login_required
from .form import boy_form, class_form, mawad_form, techer_form,absence_form,Transport_form,driver_form,masrof_form, darajat_form, absence_search
from django.db.models import Sum
from django.views.generic import UpdateView
# Create your views here.
@login_required
def classssss(request):
    return classes.objects.filter(user=request.user)
def home(request):
    return render(request, 'home/home.html')
@login_required
def boys(request):
    boys = boy.objects.filter(user=request.user).order_by('date')
    filter = BoyFilter(request.GET, queryset=boys)
    boys = filter.qs
    paginator = Paginator(boys,225)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    context = {'boys':page_pbj, 'filter':filter, 'count':boy.objects.filter(user=request.user).count()}
    return render(request, 'project/boys.html', context)
@login_required
def classs(request):
    classs = classes.objects.filter(user=request.user).order_by('date')
    filter = classFilter(request.GET, queryset=classs)
    classs = filter.qs
    paginator = Paginator(classs,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    context = {'classes':page_pbj, 'filter':filter, 'count':classes.objects.filter(user=request.user).count()}
    return render(request, 'project/classes.html', context)
@login_required
def Boy(request, id):
    Boy = boy.objects.filter(id=id, user=request.user)
    return render(request, 'project/boy_details.html', context={'boy':Boy})
@login_required
def class_detail(request, id):
    class_detail = classes.objects.filter(id=id, user=request.user)
    boys = boy.objects.filter(user=request.user)
    return render(request, 'project/class_detail.html', context={'class':class_detail, 'boy':boy.objects.filter(boy_class=id,user=request.user)})
@login_required
def techeres(request):
    techeres = techers.objects.filter(user=request.user).order_by('date')
    filter = techersFilter(request.GET, queryset=techeres)
    techeres = filter.qs
    paginator = Paginator(techeres,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request, 'project/teachers.html', context ={'teachers':page_pbj, 'filter':filter,'count': techers.objects.filter(user=request.user).count()})
@login_required
def techer_detail(request, id):
    techer_detail = techers.objects.filter(id=id, user=request.user)
    return render(request, 'project/techer_detail.html', context={'techer':techer_detail})
@login_required
def absences(request):
    absences = absence.objects.filter(user =request.user).order_by('created')
    filter = absenceFilter(request.GET, queryset=absences)
    absences = filter.qs
    paginator = Paginator(absences,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request, 'project/absences.html', context ={'absences':page_pbj, 'filter':filter,'count':absence.objects.filter(user =request.user).count()})
@login_required
def absence_detail(request, id):
    absence_detail = absence.objects.filter(id=id, user=request.user)
    return render(request, 'project/absence_detail.html', context={'absence':absence_detail})
@login_required
def driveres(request):
    driveres = driver.objects.filter(user=request.user).order_by('date')
    filter = driverFilter(request.GET, queryset=driveres)
    driveres = filter.qs
    paginator = Paginator(driveres,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request, 'project/driveres.html', context ={'driveres':page_pbj,'filter':filter, 'count':driver.objects.filter(user=request.user).count()})
@login_required
def driver_detail(request, id):
    driver_detail = driver.objects.filter(id=id, user=request.user)
    return render(request, 'project/driver_detail.html', context={'driver':driver_detail})
@login_required
def masrofs(request):
    masrofs = masrof.objects.filter(user=request.user).order_by('date')
    filter = masrofFilter(request.GET, queryset=masrofs)
    masrofs = filter.qs
    paginator = Paginator(masrofs,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request, 'project/masrofs.html', context ={'masrofs':page_pbj,'filter':filter, 'count':masrof.objects.filter(user=request.user).count()})

@login_required
def masrof_detail(request, id):
    masrof_detail = masrof.objects.filter(id=id, user=request.user)
    return render(request, 'project/masrof_detail.html', context={'masrof':masrof_detail})

@login_required
def subject(request):
    mawads = mawad.objects.filter(user=request.user).order_by('date')
    filter = mawadFilter(request.GET, queryset=mawads)
    mawads = filter.qs
    paginator = Paginator(mawads,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request, 'project/subjects.html', context ={'subjects':page_pbj,'filter':filter, 'count':mawad.objects.filter(user=request.user).count()})

@login_required
def subject_detail(request, id):
    subject_detail = mawad.objects.filter(id=id, user=request.user)
    return render(request, 'project/subject_detail.html', context={'subject':subject_detail})

@login_required
def darajats(request):
    darajats = darajat.objects.all().order_by('add_date')
    filter = darajatFilter(request.GET, queryset=darajats)
    darajats =  filter.qs
    paginator = Paginator(darajats,20)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    context = {'darajat':page_pbj, 'filter':filter, 'count':darajat.objects.filter(user=request.user).count()}
    return render(request, 'project/darajats.html', context)
@login_required
def print_all_darajat(request):
    darajats = darajat.objects.all().order_by('add_date')
    filter = darajatFilter(request.GET, queryset=darajats)
    darajats =  filter.qs
    paginator = Paginator(darajats,200)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    context = {'darajat':page_pbj, 'filter':filter}
    return render(request, 'project/all_darajats.html', context)

@login_required
def darajat_detail(request, id,profile_id):
    darajat_detail = darajat.objects.filter(id=id, user=request.user,profile=profile_id)
    return render(request, 'project/darajat_detail.html', context={'darajat':darajat_detail})

@login_required
def Transports(request):
    Transports = Transport.objects.filter(user=request.user).order_by('date')
    filter = Transport_Filter(request.GET, queryset=Transports)
    Transports =  filter.qs
    paginator = Paginator(Transports,20)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    context = {'Transports':page_pbj, 'filter':filter, 'count':Transport.objects.filter(user=request.user).count()}
    return render(request, 'project/Transports.html', context)
@login_required
def transports_detail(request, id):
    transports_detail = Transport.objects.filter(id=id, user=request.user)
    return render(request, 'project/transports_detail.html', context={'traansport':transports_detail})
@login_required
def add_boy(request):    
    if request.method=='POST':
        form = boy_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:all_boys'))

    else:
        form = boy_form()
        form.fields['boy_class'].queryset = classes.objects.filter(user=request.user)
    return render(request, 'add/add_boy.html',{'form':form})
@login_required
def add_techer(request):
    if request.method=='POST':
        form = techer_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:techeres'))

    else:
        form = techer_form()
    return render(request, 'add/techer_form.html',{'form':form})

@login_required
def add_class(request):
    if request.method=='POST':
        form = class_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:class'))
    else:
        form = class_form()
        form.fields['techer'].queryset = techers.objects.filter(user=request.user)
    return render(request, 'add/class_form.html',{'form':form})

@login_required
def add_absence(request):
    boys = boy.objects.filter(user=request.user)
    if request.method=='POST':
        form = absence_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:absence'))
    else:
        form = absence_form()
        form.fields['name'].queryset = boy.objects.filter(user=request.user)
    return render(request, 'add/absence_form.html',{'form':form, 'boys':boys})

@login_required
def add_driver(request):
    if request.method=='POST':
        form = driver_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:driveres'))
    else:
        form = driver_form()
    return render(request, 'add/driver_form.html',{'form':form})

@login_required
def add_masrof(request):
    if request.method=='POST':
        form = masrof_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:masrofs'))
    else:
        form = masrof_form()
    return render(request, 'add/masrof_form.html',{'form':form})
@login_required
def add_mawad(request):
    if request.method=='POST':
        form = mawad_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:subjects'))
    else:
        form = mawad_form()
    return render(request, 'add/mawad_form.html',{'form':form})

@login_required
def add_darajat(request):
    if request.method=='POST':
        form = darajat_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:darajats'))
    else:
        form = darajat_form()
        form.fields['name'].queryset = boy.objects.filter(user=request.user)
        form.fields['mada'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada1'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada2'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada3'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada4'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada5'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada6'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada7'].queryset = mawad.objects.filter(user=request.user)
    return render(request, 'add/darajat_form.html',{'form':form})
@login_required
def new_darajat(request, profile_id):
    my_profile = Profile.objects.get(user=request.user, id=profile_id)
    if request.method == 'POST':
        form = darajat_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = my_profile
            myform.save()
            return redirect(reverse('app:darajats'))
    else:
        form = darajat_form()
        form.fields['name'].queryset = boy.objects.filter(user=request.user)
        form.fields['mada'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada1'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada2'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada3'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada4'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada5'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada6'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada7'].queryset = mawad.objects.filter(user=request.user)
    return render(request,'project/new_darajat.html',{'form':form})
@login_required
def add_transport(request):
    if request.method=='POST':
        form = Transport_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:Transports'))
    else:
        form = Transport_form()
        form.fields['driver'].queryset = driver.objects.filter(user=request.user)
    return render(request, 'add/transport_form.html',{'form':form})
@login_required
def paid(request):
    paid1 = boy.objects.filter(user=request.user).aggregate(Sum('paid'))
    paid =  paid1['paid__sum']
    paid2 = techers.objects.filter(user=request.user).aggregate(Sum('rateb'))
    rateb =  paid2['rateb__sum']
    paid3 = driver.objects.filter(user=request.user).aggregate(Sum('rateb'))
    rateb1 =  paid3['rateb__sum']
    paid4 = masrof.objects.filter(user=request.user).aggregate(Sum('price'))
    rateb2 =  paid4['price__sum']
    rebhs = rateb + rateb1 + rateb2
    rebh = paid - rebhs
    return render(request, 'paid.html', {'paid':paid,'rateb':rateb,'driver_rateb':rateb1,'masrof':rateb2,'rebh':rebh})
@login_required
def paid_chart(request):
    paid1 = boy.objects.filter(user=request.user)
    teacher = techers.objects.filter(user=request.user)
    drivers = driver.objects.filter(user=request.user)
    masrofs = masrof.objects.filter(user=request.user)
    paid4 = masrof.objects.filter(user=request.user).aggregate(Sum('price'))
    rateb2 =  paid4['price__sum']
    paid2 = techers.objects.filter(user=request.user).aggregate(Sum('rateb'))
    rateb =  paid2['rateb__sum']
    paid3 = driver.objects.filter(user=request.user).aggregate(Sum('rateb'))
    rateb1 =  paid3['rateb__sum']
    rebhs = rateb + rateb1 + rateb2
    paids = boy.objects.filter(user=request.user).aggregate(Sum('paid'))
    total =  paids['paid__sum']
    profits = total - rebhs
    context = {
        'boys':paid1,
        'techers':teacher,
        'drivers':drivers,
        'masrofs':masrofs,
        'total_masrofs':rateb2,
        'total_techers':rateb,
        'total_drivers':rateb1,
        'paids':rebhs,
        'total':total,
        'profits':profits,
    }
    return render(request,'paid.html',context)
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request ,'profile.html', {'profile': profile})
@login_required
class BoyEdit(UpdateView):
    model = boy
    fields = ('name', 'age','boy_class','number_kawme','number_phone','image','paid',)
    template_name= 'edit/edit_boy.html'
    pk_url_kwarg= 'id'
    context_object_name = 'boy'
    def form_valid(self, form):
        boy = form.save(commit=False)
        boy.user = self.request.user
        boy.save()
        return redirect('app:all_boys')
@login_required
def edit_boy(request, id):
    boys = boy.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = boy_form(request.POST, request.FILES, instance=boys)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:all_boys'))

    else:
        form = boy_form(instance=boys)
        form.fields['boy_class'].queryset = classes.objects.filter(user=request.user)
    return render(request, 'edit/edit_boy.html',{'form':form})

@login_required
def edit_class(request, id):
    classe = classes.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = class_form(
            request.POST, request.FILES, instance=classe)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:class'))

    else:
        form = class_form(instance=classe)
        form.fields['techer'].queryset = techers.objects.filter(user=request.user)
    return render(request, 'edit/edit_class.html',{'form':form})

@login_required
def edit_techer(request,id):
    techer = techers.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = techer_form(request.POST, request.FILES, instance=techer)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:techeres'))

    else:
        form = techer_form(instance=techer)
    return render(request, 'edit/edit_teacher.html',{'form':form})

@login_required
def edit_absence(request,id):
    absences = absence.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = absence_form(request.POST, request.FILES, instance=absences)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:absence'))

    else:
        form = absence_form(instance=absences)
        form.fields['name'].queryset = boy.objects.filter(user=request.user)
    return render(request, 'edit/edit_absence.html',{'form':form})

@login_required
def edit_masrof(request,id):
    masrofs = masrof.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = masrof_form(request.POST, request.FILES, instance=masrofs)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:masrofs'))
    else:
        form = masrof_form(instance=masrofs)
    return render(request, 'edit/edit_masrof.html',{'form':form})

@login_required
def edit_driver(request,id):
    drivers = driver.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = driver_form(request.POST, request.FILES,instance=drivers)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:driveres'))
    else:
        form = driver_form(instance=drivers)
    return render(request, 'edit/edit_driver.html',{'form':form})

@login_required
def edit_subject(request,id):
    subject = mawad.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = mawad_form(request.POST, request.FILES, instance=subject)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:techeres'))

    else:
        form = mawad_form(instance=subject)
    return render(request, 'edit/edit_subject.html',{'form':form})

@login_required
def edit_darajat(request,id):
    darajats = darajat.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = darajat_form(request.POST, request.FILES, instance=darajats)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:darajats'))

    else:
        form = darajat_form(instance=darajats)
        form.fields['name'].queryset = boy.objects.filter(user=request.user)
        form.fields['mada'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada1'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada2'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada3'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada4'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada5'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada6'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada7'].queryset = mawad.objects.filter(user=request.user)
    return render(request, 'edit/edit_darajat.html',{'form':form})

@login_required
def edit_transport(request,id):
    transportes = Transport.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = Transport_form(request.POST, request.FILES,instance=transportes)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:Transports'))
    else:
        form = Transport_form(instance=transportes)
        form.fields['driver'].queryset = driver.objects.filter(user=request.user)
    return render(request, 'edit/edit_transport.html',{'form':form})
@login_required
def delete_boy(request, id):
    boys = boy.objects.get(id=id, user=request.user)
    boys.delete()
    return redirect('app:all_boys')
@login_required
def delete_class(request, id):
    classe = classes.objects.get(id=id, user=request.user)
    classe.delete()
    return redirect('app:class')
@login_required
def delete_techer(request, id):
    techer = techers.objects.get(id=id, user=request.user)
    techer.delete()
    return redirect('app:techeres')
@login_required
def delete_absences(request, id):
    absences = absence.objects.get(id=id, user=request.user)
    absences.delete()
    return redirect('app:absence')
@login_required
def delete_subject(request, id):
    subject = mawad.objects.get(id=id, user=request.user)
    subject.delete()
    return redirect('app:subjects')
@login_required
def delete_driver(request, id):
    drivers = driver.objects.get(id=id, user=request.user)
    drivers.delete()
    return redirect('app:driveres')
@login_required
def delete_masrof(request, id):
    masrofs = masrof.objects.get(id=id, user=request.user)
    masrofs.delete()
    return redirect('app:masrofs')
@login_required
def delete_transport(request, id):
    delete_transport = Transport.objects.get(id=id, user=request.user)
    delete_transport.delete()
    return redirect('app:Transports')
@login_required
def delete_darajat(request, id):
    delete_darajat = darajat.objects.get(id=id, user=request.user)
    delete_darajat.delete()
    return redirect('app:darajats')