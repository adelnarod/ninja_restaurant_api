# Generated by Django 4.1.1 on 2022-09-19 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0004_ingredient_dishes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('restaurant_type', models.CharField(max_length=64)),
                ('rating', models.IntegerField(default=0)),
                ('search_terms', models.CharField(default='<django.db.models.fields.CharField>,<django.db.models.fields.CharField>', max_length=500)),
                ('menu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='menu.menu')),
            ],
        ),
    ]
