# Generated by Django 5.0.1 on 2024-01-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=13, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('genre', models.CharField(max_length=20)),
                ('rating', models.FloatField(default=0.0)),
                ('num_pages', models.PositiveIntegerField()),
            ],
        ),
    ]
