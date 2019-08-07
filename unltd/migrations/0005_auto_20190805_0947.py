# Generated by Django 2.2.1 on 2019-08-05 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unltd', '0004_vendormember_vendorstaff'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='vendor',
            field=models.ForeignKey(db_column='VendorId', default=1, on_delete=django.db.models.deletion.CASCADE, to='unltd.VendorStaff'),
        ),
        migrations.AddField(
            model_name='staff',
            name='vendor',
            field=models.ForeignKey(db_column='VendorId', default=1, on_delete=django.db.models.deletion.CASCADE, to='unltd.VendorStaff'),
        ),
        migrations.AlterField(
            model_name='member',
            name='userid',
            field=models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, to='unltd.User'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='userid',
            field=models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, to='unltd.User'),
        ),
        migrations.CreateModel(
            name='VendorDiscount',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', default=None, max_length=225)),
                ('discount', models.IntegerField(db_column='Discount')),
                ('createdat', models.DateTimeField(auto_now=True, db_column='CreatedDate')),
                ('expirydate', models.DateTimeField(auto_now=True, db_column='ExpiryDate')),
                ('userid', models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.CASCADE, to='unltd.User')),
            ],
        ),
    ]