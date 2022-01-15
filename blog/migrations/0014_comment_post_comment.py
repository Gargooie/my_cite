# Generated by Django 4.0.1 on 2022-01-10 08:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('comment_text', models.TextField(validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(500)])),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
        ),
    ]