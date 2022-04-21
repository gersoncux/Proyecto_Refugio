# Generated by Django 4.0.3 on 2022-04-17 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'CategoriaMascota',
                'verbose_name_plural': 'CategoriasMascota',
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='albergue')),
                ('disponibilidad', models.BooleanField(default=True)),
                ('alimentacion', models.CharField(blank=True, max_length=50, null=True)),
                ('vacunas', models.CharField(max_length=60)),
                ('raza', models.CharField(max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albergue.categoriamascota')),
            ],
            options={
                'verbose_name': 'Mascota',
                'verbose_name_plural': 'Mascotas',
            },
        ),
    ]
