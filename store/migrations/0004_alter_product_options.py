# Generated by Django 4.2 on 2023-07-07 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_reviewrating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-modified_date']},
        ),
    ]
