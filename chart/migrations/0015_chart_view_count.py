# Generated by Django 4.1.2 on 2022-11-12 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0014_remove_element_created_on_chart_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
