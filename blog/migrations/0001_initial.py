# Generated by Django 3.1.2 on 2020-11-11 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IATA', models.CharField(max_length=4)),
                ('IACO', models.CharField(max_length=4)),
            ],
        ),
    ]
