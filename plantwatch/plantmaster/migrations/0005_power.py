# Generated by Django 3.0.5 on 2020-05-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantmaster', '0004_delete_adresses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('powerid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('producedat', models.DateTimeField()),
                ('power', models.IntegerField()),
            ],
            options={
                'db_table': 'power',
                'managed': False,
            },
        ),
    ]
