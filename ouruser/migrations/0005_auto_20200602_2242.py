# Generated by Django 3.0.5 on 2020-06-02 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ouruser', '0004_auto_20200318_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userschool',
            field=models.TextField(max_length=32, verbose_name='소속'),
        ),
    ]