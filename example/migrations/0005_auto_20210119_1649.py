# Generated by Django 3.1.5 on 2021-01-19 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0004_auto_20210119_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='id',
        ),
        migrations.AddField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default=None, max_length=1),
        ),
    ]
