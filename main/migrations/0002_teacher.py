# Generated by Django 2.2.4 on 2019-08-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dept', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
            ],
        ),
    ]
