# Generated by Django 2.2.1 on 2019-08-05 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unltd', '0005_auto_20190805_0947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendordiscount',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='vendordiscount',
            table='VendorDiscount',
        ),
        migrations.CreateModel(
            name='Itemofferoption',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('customoffer', models.CharField(db_column='CustomOffer', max_length=225)),
                ('price', models.IntegerField(db_column='Price', default=None)),
                ('startdate', models.DateTimeField(db_column='StartTimeRange', default=None)),
                ('enddate', models.DateTimeField(db_column='EndTimeRange', default=None)),
                ('creationdate', models.DateTimeField(auto_now=True, db_column='CreatedDate')),
                ('itemid', models.ForeignKey(db_column='ItemId', on_delete=django.db.models.deletion.CASCADE, to='unltd.Item')),
            ],
            options={
                'db_table': 'itemofferoption',
                'managed': True,
            },
        ),
    ]
