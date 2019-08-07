# Generated by Django 2.2.1 on 2019-08-05 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unltd', '0002_backup'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialType',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', default=None, max_length=255)),
            ],
            options={
                'db_table': 'tutorialtype',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='tutorial',
            name='group',
            field=models.CharField(db_column='group', default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='created_by',
            field=models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.DO_NOTHING, to='unltd.User'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='type',
            field=models.ForeignKey(db_column='type', default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='tutorialtype', to='unltd.TutorialType'),
            preserve_default=False,
        ),
    ]
