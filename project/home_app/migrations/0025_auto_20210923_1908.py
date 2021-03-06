# Generated by Django 3.2.7 on 2021-09-23 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_app', '0024_auto_20210921_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='darajat',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='المستخدم'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mawad',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='المستخدم'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('tok tok', 'tok tok'), ('car', 'car'), ('bus', 'bus')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
    ]
