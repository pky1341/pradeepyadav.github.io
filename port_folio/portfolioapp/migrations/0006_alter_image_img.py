# Generated by Django 4.1.1 on 2022-10-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0005_alter_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]