# Generated by Django 3.2.6 on 2021-09-03 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20210902_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.cartitem')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.customeruser')),
            ],
        ),
    ]
