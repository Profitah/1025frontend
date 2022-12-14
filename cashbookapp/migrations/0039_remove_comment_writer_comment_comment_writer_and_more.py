# Generated by Django 4.1.2 on 2022-10-29 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cashbookapp', '0038_rename_comment_writer_comment_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='writer',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='댓글 작성자'),
        ),
        migrations.AlterField(
            model_name='cashbook',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]
