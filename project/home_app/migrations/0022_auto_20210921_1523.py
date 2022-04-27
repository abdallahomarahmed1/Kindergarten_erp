# Generated by Django 3.2.7 on 2021-09-21 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0021_auto_20210921_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mawad',
            name='daraja',
            field=models.IntegerField(verbose_name='الدرجة النهائية'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('car', 'car'), ('bus', 'bus'), ('tok tok', 'tok tok')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
        migrations.CreateModel(
            name='darajat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daraja', models.IntegerField(verbose_name='درجة الطالب')),
                ('daraja1', models.IntegerField(verbose_name='درجة الطالب')),
                ('daraja2', models.IntegerField(verbose_name='درجة الطالب')),
                ('daraja3', models.IntegerField(verbose_name='درجة الطالب')),
                ('daraja4', models.IntegerField(verbose_name='درجة الطالب')),
                ('daraja5', models.IntegerField(verbose_name='درجة الطالب')),
                ('mada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.mawad', verbose_name='المادة')),
                ('mada1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mada1', to='home_app.mawad', verbose_name='المادة')),
                ('mada2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mada2', to='home_app.mawad', verbose_name='المادة')),
                ('mada3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mada3', to='home_app.mawad', verbose_name='المادة')),
                ('mada4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mada4', to='home_app.mawad', verbose_name='المادة')),
                ('mada5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mada5', to='home_app.mawad', verbose_name='المادة')),
            ],
        ),
    ]
