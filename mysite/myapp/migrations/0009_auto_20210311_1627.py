# Generated by Django 3.1.7 on 2021-03-11 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210311_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='designation_name',
        ),
        migrations.AddField(
            model_name='designations',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.companies'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='designation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.designations'),
            preserve_default=False,
        ),
    ]