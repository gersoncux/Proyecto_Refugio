# Generated by Django 4.0.3 on 2022-04-17 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RefugiowebApp', '0005_alter_datos_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos',
            name='update',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]