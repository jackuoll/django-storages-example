# Generated by Django 2.0.7 on 2018-07-31 06:06

import custom_storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploadInAnotherBucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_in_other_bucket', models.FileField(storage=custom_storage.TotallyOtherPrivateStorage(), upload_to='')),
            ],
        ),
    ]