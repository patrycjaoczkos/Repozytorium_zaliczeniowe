# Generated by Django 5.1.3 on 2025-01-16 20:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0008_osoba_wlasciciel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='stanowisko',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='folder_aplikacji.stanowisko'),
        ),
    ]
