# Generated by Django 4.0.1 on 2022-01-27 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0034_remove_techers_her_class_alter_transport_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boy',
            name='boy_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home_app.classes', verbose_name='الفصل'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('تكتك', 'تكتك'), ('ميكروباس', 'ميكروباس'), ('اتوبيس', 'اتوبيس'), ('سيارة', 'سيارة')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
    ]