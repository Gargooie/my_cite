# Generated by Django 3.2.9 on 2022-01-06 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220106_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
