# Generated by Django 5.1.3 on 2025-01-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0004_osoba_data_dodania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='plec',
            field=models.IntegerField(choices=[(1, 'Kobieta'), (2, 'Mężczyzna'), (3, 'Inna')], default=3),
        ),
    ]
