# Generated by Django 5.0.9 on 2024-09-06 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.topic'),
        ),
        migrations.AlterField(
            model_name='joinrequest',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.topic'),
        ),
        migrations.AlterField(
            model_name='joinrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
