# Generated by Django 3.0.7 on 2020-06-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='context',
            field=models.TextField(blank=True, null=True),
        ),
    ]