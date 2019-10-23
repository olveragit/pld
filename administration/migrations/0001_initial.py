# Generated by Django 2.2.6 on 2019-10-22 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=40)),
                ('last_name', models.CharField(help_text='Last name', max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]