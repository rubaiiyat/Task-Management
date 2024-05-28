# Generated by Django 5.0.2 on 2024-05-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=50)),
                ('taskDescription', models.CharField(max_length=50)),
                ('boolean', models.BooleanField(default=False)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
