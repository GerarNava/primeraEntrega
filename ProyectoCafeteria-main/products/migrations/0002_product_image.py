# Generated by Django 4.2.5 on 2023-10-04 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
