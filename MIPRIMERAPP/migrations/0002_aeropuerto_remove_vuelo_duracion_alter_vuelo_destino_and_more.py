# Generated by Django 4.0.4 on 2023-05-03 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MIPRIMERAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3)),
                ('ciudad', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='vuelo',
            name='duracion',
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='llegadas', to='MIPRIMERAPP.aeropuerto'),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salidas', to='MIPRIMERAPP.aeropuerto'),
        ),
    ]
