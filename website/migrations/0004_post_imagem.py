# Generated by Django 3.1a1 on 2020-05-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200519_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
