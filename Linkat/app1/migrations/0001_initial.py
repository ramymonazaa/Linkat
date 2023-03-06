# Generated by Django 2.2.5 on 2022-09-20 12:53

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='undefiend', max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('rate', models.IntegerField(default=0, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app1.Category')),
            ],
            options={
                'verbose_name': 'Link',
                'ordering': ['rate', 'name'],
            },
        ),
    ]
