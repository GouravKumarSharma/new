# Generated by Django 3.2.13 on 2022-07-10 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adpost',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=2000)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='contectform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=200)),
                ('mobile', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='jdregister',
            fields=[
                ('userid', models.IntegerField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='jduser',
            fields=[
                ('userid', models.IntegerField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='jdpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=1000)),
                ('time', models.DateField()),
                ('rank', models.IntegerField(max_length=2)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jduser')),
            ],
        ),
    ]
