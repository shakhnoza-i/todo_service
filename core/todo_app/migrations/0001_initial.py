# Generated by Django 4.0.5 on 2022-06-15 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=255)),
                ('complete_time', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
