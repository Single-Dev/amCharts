# Generated by Django 4.1.2 on 2022-12-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0026_remove_chart_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
    ]