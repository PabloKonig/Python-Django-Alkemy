# Generated by Django 5.0.4 on 2024-04-19 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0003_autor_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='foto',
            field=models.ImageField(default='autor_generico.png', upload_to='autores_img/'),
        ),
    ]
