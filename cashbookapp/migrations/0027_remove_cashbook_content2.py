# Generated by Django 4.0.4 on 2022-10-01 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0026_cashbook_content2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashbook',
            name='content2',
        ),
    ]