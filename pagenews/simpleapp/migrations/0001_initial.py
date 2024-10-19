# Generated by Django 4.2.16 on 2024-10-11 14:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_news', models.CharField(max_length=64, unique=True)),
                ('description_news', models.TextField()),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('cost_news', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('category_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='simpleapp.category')),
            ],
        ),
    ]
