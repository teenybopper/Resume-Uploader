# Generated by Django 4.2.5 on 2023-11-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_uploader_gender_alter_uploader_job_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploader',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
