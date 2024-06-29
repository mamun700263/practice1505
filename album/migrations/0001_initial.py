# Generated by Django 5.0.4 on 2024-06-29 01:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album_name', models.CharField(max_length=100)),
                ('Album_release_date', models.DateField()),
                ('Album_Rating', models.CharField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], max_length=5)),
                ('Album_musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musician')),
            ],
        ),
    ]