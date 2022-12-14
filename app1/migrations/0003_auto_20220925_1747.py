# Generated by Django 2.2.5 on 2022-09-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_product_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-rate', 'name'], 'verbose_name': 'Link'},
        ),
        migrations.AlterField(
            model_name='product',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/%y/%m/%d'),
        ),
    ]
