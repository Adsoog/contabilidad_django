# Generated by Django 5.0.2 on 2024-02-11 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=225)),
                ('age', models.CharField(max_length=225)),
                ('monthly_salary', models.CharField(max_length=1000)),
            ],
        ),
    ]
