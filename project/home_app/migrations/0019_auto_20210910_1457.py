# Generated by Django 3.2.7 on 2021-09-10 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0018_auto_20210909_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='absence',
            name='add_date',
            field=models.DateField(blank=True, null=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='absence',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='boy',
            name='add_date',
            field=models.DateField(blank=True, null=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='boy',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='classes',
            name='add_date',
            field=models.DateField(blank=True, null=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='classes',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='driver',
            name='add_date',
            field=models.DateField(blank=True, null=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='masrof',
            name='add_date',
            field=models.DateField(blank=True, null=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='masrof',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='techers',
            name='add_date',
            field=models.DateField(blank=True, null=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='techers',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='transport',
            name='add_date',
            field=models.DateField(blank=True, null=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='transport',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='التاريخ'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('tok tok', 'tok tok'), ('car', 'car'), ('bus', 'bus')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
    ]
