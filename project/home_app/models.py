# from typing import Reversible
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
kind_of_Transport = {
    ('اتوبيس','اتوبيس'),
    ('سيارة','سيارة'),
    ('تكتك', 'تكتك'),
    ('ميكروباس','ميكروباس'),
}

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="اسم الروضة")
    city = models.CharField(max_length=50, verbose_name="العنوان")
    name_of_admin = models.CharField(max_length=50, verbose_name="اسم المشرف")
    phone_number = models.IntegerField(verbose_name="رقم الهاتف", blank=True, null=True)
    img = models.ImageField(upload_to="user_img/", verbose_name="شعار الروضة")

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return str(self.user)

    # def get_absolute_url(self):
    #     return reverse("Profile_detail", kwargs={"pk": self.pk})
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
class boy(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="الاسم")
    age = models.IntegerField(verbose_name="السن")
    boy_class = models.ForeignKey("classes", verbose_name=("الفصل"), on_delete=models.PROTECT)
    number_kawme = models.IntegerField(verbose_name="الرقم القومي")
    number_phone = models.IntegerField(verbose_name="رقم الوالد او الوالدة")
    image = models.ImageField(upload_to="boys_images/", verbose_name="صورة الطفل", blank=True, null=True)
    paid = models.IntegerField(verbose_name='المبلغ المدفع')
    date = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    add_date = models.DateField(auto_now=False,auto_now_add=False,verbose_name="التاريخ",null=True,blank=True)
    def __str__(self):
        return self.name
    def classs(self):
        self.boy_class.all()

class classes(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="اسم الفصل")
    techer = models.ForeignKey("techers", verbose_name=("المعلمة"), on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)

    def __str__(self):
        return self.name
class techers(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="الاسم")
    age = models.IntegerField(verbose_name="السن")
    qualification = models.CharField(max_length=50, verbose_name="المؤهل")
    number_kawme = models.IntegerField(verbose_name="الرقم القومي")
    Salary = models.IntegerField(verbose_name="المرتب الشهري")
    number_phone = models.IntegerField(verbose_name="رقم هاتف المعلمة")
    rateb = models.IntegerField(verbose_name="الراتب السنوي", null=True ,blank=True)
    date = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)
    def save(self, *args, **kwargs):
        cwn = self.Salary * 6
        self.rateb = cwn
        super(techers, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'techers'

class absence(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.ForeignKey("boy", verbose_name="الاسم", on_delete=models.CASCADE)
    excuse = models.BooleanField(default=True, verbose_name=("بعذر ام لا"))
    created = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = ("absence")
        verbose_name_plural = ("absences")
        

    def get_absolute_url(self):
        return Reversible("absence_detail", kwargs={"pk": self.pk})

class Transport(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    kind = models.CharField(max_length=50, choices=kind_of_Transport, verbose_name=("نوع وسيلة النقل"))
    driver = models.OneToOneField("driver", verbose_name=("السائق"), on_delete=models.CASCADE)
    number = models.CharField(max_length=20, verbose_name="الرقم التعريفي")
    date = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)
    class Meta:
        verbose_name = ("Transport")
        verbose_name_plural = ("Transports")

    def __str__(self):
        return self.number

    # def get_absolute_url(self):
    #     return reverse("Transport_detail", kwargs={"pk": self.pk})

class driver(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="الاسم")
    number_kawme = models.IntegerField(verbose_name="الرقم القومي")
    number_phone = models.IntegerField(verbose_name="رقم الهاتف")
    Salary = models.IntegerField(verbose_name="المرتب الشهري")
    image = models.ImageField(upload_to="boys_images/", verbose_name="صورة السائق", blank=True, null=True)
    rateb = models.IntegerField(verbose_name="الراتب السنوي", null=True ,blank=True)
    date = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)
    def save(self, *args, **kwargs):
        cwn = self.Salary * 6
        self.rateb = cwn
        super(driver, self).save(*args, **kwargs)
    def __str__(self):
       return self.name

    class Meta:
        verbose_name = 'driver'
        verbose_name_plural = 'drivers'
class masrof(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="المصروف")
    price = models.IntegerField(verbose_name="السعر")
    date = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)
    class Meta:
        verbose_name = ("masrof")
        verbose_name_plural = ("masrofs")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("masrof_detail", kwargs={"pk": self.pk})

class mawad(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='اسم المادة')
    daraja = models.IntegerField(verbose_name='الدرجة النهائية')
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class darajat(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.ForeignKey(boy, verbose_name=("اسم الطالب"), on_delete=models.CASCADE, null=True)
    mada = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE)
    daraja = models.IntegerField(verbose_name='درجة الطالب')
    mada1 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada1')
    daraja1 = models.IntegerField(verbose_name='درجة الطالب')
    mada2 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada2')
    daraja2 = models.IntegerField(verbose_name='درجة الطالب')
    mada3 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada3')
    daraja3 = models.IntegerField(verbose_name='درجة الطالب')
    mada4 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada4',null=True,blank=True)
    daraja4 = models.IntegerField(verbose_name='درجة الطالب' ,null=True, default='0')
    mada5 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada5',null=True,blank=True)
    daraja5 = models.IntegerField(verbose_name='درجة الطالب' ,null=True, default='0')
    mada6 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada6',null=True,blank=True)
    daraja6 = models.IntegerField(verbose_name='درجة الطالب',null=True, default='0')
    mada7 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada7',null=True,blank=True)
    daraja7 = models.IntegerField(verbose_name='درجة الطالب',null=True, default='0')
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)
    def ejmale(self):
        ejmale = self.daraja + self.daraja1 + self.daraja2 +self.daraja3 + self.daraja4 + self.daraja5 + self.daraja6 + self.daraja6
        if self.daraja5:
            ejmale += self.daraja5
        if self.daraja6:
            ejmale += self.daraja6
        if self.daraja4:
            ejmale += self.daraja4
        if self.daraja7:
            ejmale += self.daraja7
        return ejmale
    def total(self):
        ejmale = self.mada.daraja + self.mada1.daraja + self.mada2.daraja + self.mada3.daraja
        if self.mada4.daraja:
            ejmale += self.mada4.daraja
        if self.mada5.daraja:
            ejmale += self.mada5.daraja 
        if self.mada6:
           ejmale += self.mada6.daraja
        return ejmale
    def nesba(self):
        self_darajat = self.ejmale()
        total = self.total()
        return self_darajat / total
    def __str__(self):
        return str(self.name)


