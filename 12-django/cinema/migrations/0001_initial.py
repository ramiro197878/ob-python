# Generated by Django 4.0.4 on 2022-05-29 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre del director', max_length=64)),
                ('lastname', models.CharField(help_text='Apellido del director', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Nombre de la pelicula', max_length=64)),
                ('description', models.TextField(help_text='Descripcion', max_length=500)),
                ('year', models.IntegerField()),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.directors')),
            ],
        ),
    ]