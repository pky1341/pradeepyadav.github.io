# Generated by Django 4.1.1 on 2022-10-02 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0008_alter_image_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='personal')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]