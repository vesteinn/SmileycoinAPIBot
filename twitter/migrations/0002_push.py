# Generated by Django 2.2.6 on 2019-10-28 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Push',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_height', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
