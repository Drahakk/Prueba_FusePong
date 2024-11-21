# Generated by Django 5.1.3 on 2024-11-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='D',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
                ('descripcion', models.TextField(blank=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='T',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('tituloticket', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descripcionticket', models.TextField(blank=True, verbose_name='Descripción')),
                ('estadoticket', models.CharField(max_length=100, verbose_name='Estado')),
            ],
        ),
    ]
