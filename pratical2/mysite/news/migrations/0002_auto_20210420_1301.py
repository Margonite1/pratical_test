# Generated by Django 2.2.17 on 2021-04-20 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='News_Item',
        ),
    ]
