# Generated by Django 4.1.1 on 2022-10-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0007_alter_image_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
