# Generated by Django 3.0.7 on 2020-07-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_post_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='def.png', upload_to='Posts/'),
        ),
    ]
