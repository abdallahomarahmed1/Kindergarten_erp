# Generated by Django 3.2.6 on 2021-08-18 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0006_auto_20210818_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='masrof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='المصروف')),
                ('price', models.IntegerField(verbose_name='السعر')),
            ],
            options={
                'verbose_name': 'masrof',
                'verbose_name_plural': 'masrofs',
            },
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'driver', 'verbose_name_plural': 'drivers'},
        ),
        migrations.AlterModelTable(
            name='driver',
            table=None,
        ),
    ]
