# Generated by Django 2.2.14 on 2020-08-18 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created', 'title')},
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_header',
            field=models.ImageField(default='posts/photos/ Sin título.png', upload_to='posts/photos'),
        ),
        migrations.AlterField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.SlugField(unique=True),
        ),
    ]
