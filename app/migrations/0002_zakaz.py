# Generated by Django 4.2.7 on 2023-11-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('items', models.TextField()),
            ],
        ),
    ]
