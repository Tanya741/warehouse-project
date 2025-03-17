# Generated by Django 5.1.7 on 2025-03-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('brand', models.CharField(max_length=70)),
                ('quantity', models.IntegerField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
