# Generated by Django 5.1.1 on 2024-09-17 14:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_quran_mood_intensity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quran',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
