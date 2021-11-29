# Generated by Django 3.2.9 on 2021-11-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogarticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('story', models.CharField(max_length=9000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('refid', models.CharField(default='', editable=False, max_length=5000)),
            ],
            options={
                'db_table': 'blogarticle',
            },
        ),
    ]