# Generated by Django 4.1.7 on 2023-03-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_remove_listing_like_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='hometown',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
