# Generated by Django 4.1.1 on 2022-10-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0020_etc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.TextField()),
            ],
        ),
    ]
