# Generated by Django 3.2.6 on 2021-08-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210830_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
