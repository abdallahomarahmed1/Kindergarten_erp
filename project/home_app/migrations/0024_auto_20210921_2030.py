# Generated by Django 3.2.7 on 2021-09-21 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0023_auto_20210921_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='darajat',
            name='daraja6',
            field=models.IntegerField(default='1', verbose_name='درجة الطالب'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='darajat',
            name='daraja7',
            field=models.IntegerField(default='1', verbose_name='درجة الطالب'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='darajat',
            name='mada6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mada6', to='home_app.mawad', verbose_name='المادة'),
        ),
        migrations.AddField(
            model_name='darajat',
            name='mada7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mada7', to='home_app.mawad', verbose_name='المادة'),
        ),
        migrations.AlterField(
            model_name='darajat',
            name='mada4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mada4', to='home_app.mawad', verbose_name='المادة'),
        ),
        migrations.AlterField(
            model_name='darajat',
            name='mada5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mada5', to='home_app.mawad', verbose_name='المادة'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('tok tok', 'tok tok'), ('bus', 'bus'), ('car', 'car')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
    ]
