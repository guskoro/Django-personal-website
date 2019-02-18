# Generated by Django 2.1.5 on 2019-02-16 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190215_0902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='time',
            new_name='publish',
        ),
        migrations.AddField(
            model_name='post',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
    ]