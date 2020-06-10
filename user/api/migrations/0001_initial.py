# Generated by Django 3.0.6 on 2020-06-06 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('permission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('firtsname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Role')),
            ],
        ),
    ]
