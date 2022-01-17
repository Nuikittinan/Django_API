# Generated by Django 3.2 on 2021-12-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceAll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(blank=True, null=True)),
                ('spo2', models.IntegerField(blank=True, null=True)),
                ('hr', models.IntegerField(blank=True, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField(blank=True, null=True)),
                ('birthday', models.TextField(blank=True, null=True)),
                ('age', models.TextField(blank=True, null=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
