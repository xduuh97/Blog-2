# Generated by Django 3.1a1 on 2020-05-19 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_post_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='conteudo',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='sub_title',
            new_name='sub_titulo',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='post',
            name='categorias',
            field=models.CharField(choices=[('GR', 'Geral'), ('EVT', 'Eventos'), ('CUL', 'Cultos'), ('CR', 'Curiosidades'), ('PB', 'Passagens Bíblicas')], default='GR', max_length=4),
        ),
    ]
