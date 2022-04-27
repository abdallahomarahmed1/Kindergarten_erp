# Generated by Django 3.2.6 on 2021-08-29 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_app', '0011_auto_20210819_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='absence',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='المستخدم'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='masrof',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='المستخدم'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('bus', 'bus'), ('car', 'car'), ('tok tok', 'tok tok')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
    ]