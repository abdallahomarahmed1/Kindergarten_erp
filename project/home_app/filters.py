import django_filters
from .models import boy,classes,techers,absence,Transport,driver,masrof,Profile, mawad,darajat

class BoyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = boy
        fields = ['name', 'age', 'boy_class', 'number_kawme', 'number_phone']

class classFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = classes
        fields = ['name', 'techer']
class techersFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = techers
        fields = ['name', 'age', 'qualification', 'number_kawme','Salary','number_phone']
class absenceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    created = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))
    class Meta:
        model = absence
        fields = ['name', 'excuse','created']
class masrofFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = masrof
        fields = ['name', 'price']

class driverFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = driver
        fields = ['name', 'number_kawme', 'number_phone', 'Salary']

class transportFilter(django_filters.FilterSet):
    driver = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Transport
        fields = ['kind', 'driver', 'number']

class mawadFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    # date = django_filters.DateFilter(widget=django_filters.(attrs={'type': 'date'}))
    class Meta:
        model = mawad
        fields = '__all__'
        exclude = ('user')

class darajatFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = darajat
        fields = ['name']
class Transport_Filter(django_filters.FilterSet):
    # driver = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Transport
        fields = '__all__'
        exclude = ('user','date', 'add_date')
