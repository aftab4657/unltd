# Generated by Django 2.2.1 on 2019-08-06 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unltd', '0006_auto_20190805_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendordiscount',
            name='type',
            field=models.CharField(db_column='Type', default='FixedAmount', max_length=225),
        ),
        migrations.AlterField(
            model_name='vendordiscount',
            name='expirydate',
            field=models.DateTimeField(db_column='ExpiryDate'),
        ),
    ]
