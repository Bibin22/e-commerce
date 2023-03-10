# Generated by Django 4.1.5 on 2023-01-04 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('strap_color', models.CharField(max_length=20)),
                ('highlight', models.TextField()),
                ('price', models.IntegerField()),
                ('active_inactive', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
