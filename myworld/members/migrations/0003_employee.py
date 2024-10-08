# Generated by Django 5.1.1 on 2024-10-04 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_students_delete_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=10)),
                ('salary', models.IntegerField()),
                ('department', models.CharField(max_length=10)),
            ],
        ),
    ]
