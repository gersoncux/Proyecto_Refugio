# Generated by Django 4.0.3 on 2022-04-11 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('raza', models.CharField(max_length=50)),
                ('alimento', models.CharField(max_length=50)),
                ('enfermedad', models.BooleanField()),
                ('vacunas', models.BooleanField()),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]