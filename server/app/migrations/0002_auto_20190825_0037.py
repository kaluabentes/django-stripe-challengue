# Generated by Django 2.2.4 on 2019-08-25 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='option',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
