# Generated by Django 5.0.3 on 2024-03-22 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('division', models.CharField(max_length=100)),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('injured_resv_list', models.BooleanField()),
                ('pass_yds', models.IntegerField()),
                ('rush_yds', models.IntegerField()),
                ('rec', models.IntegerField()),
                ('tackles', models.IntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='teams.team')),
            ],
        ),
    ]