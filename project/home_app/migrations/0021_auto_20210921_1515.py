# Generated by Django 3.2.7 on 2021-09-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0020_auto_20210918_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='mawad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='اسم المادة')),
                ('daraja', models.IntegerField(verbose_name='الدرة النهائية')),
            ],
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('bus', 'bus'), ('tok tok', 'tok tok'), ('car', 'car')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
    ]
