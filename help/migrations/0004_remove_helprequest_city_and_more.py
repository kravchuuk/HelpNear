# Generated by Django 5.1.7 on 2025-04-09 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0003_helprequest_city_alter_helprequest_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helprequest',
            name='city',
        ),
        migrations.AddField(
            model_name='helprequest',
            name='accepted_response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accepted_for', to='help.helpresponse'),
        ),
        migrations.AddField(
            model_name='helprequest',
            name='detailed_expectation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='helpresponse',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='helprequest',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]
