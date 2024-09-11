# Generated by Django 5.1.1 on 2024-09-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('stock', models.IntegerField(default=0)),
                ('publisher', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('mood_intensity', models.IntegerField()),
            ],
        ),
    ]