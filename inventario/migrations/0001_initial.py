# Generated by Django 5.0.2 on 2024-02-11 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sap', models.CharField(max_length=150)),
                ('item', models.CharField(max_length=200)),
                ('precio_unitario', models.CharField(max_length=10000)),
            ],
        ),
    ]
