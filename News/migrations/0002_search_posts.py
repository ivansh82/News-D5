# Generated by Django 3.2 on 2021-04-08 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='posts',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='News.posts'),
        ),
    ]