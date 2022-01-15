# Generated by Django 3.2.9 on 2022-01-06 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='blog/')),
                ('author', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('excerpt', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
    ]
