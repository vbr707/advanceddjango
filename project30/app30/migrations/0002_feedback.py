# Generated by Django 2.1.7 on 2019-03-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app30', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('un', models.CharField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
    ]