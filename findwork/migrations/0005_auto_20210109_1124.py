# Generated by Django 3.1.3 on 2021-01-09 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findwork', '0004_auto_20210108_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('F', 'Female')], max_length=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('employer', '1'), ('employee', '2')], max_length=10),
        ),
    ]
