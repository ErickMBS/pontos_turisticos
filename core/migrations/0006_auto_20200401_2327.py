# Generated by Django 2.0.4 on 2020-04-02 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_pontoturistico_endereco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontoturistico',
            name='localizacao',
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='aprovado',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='descricao',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
