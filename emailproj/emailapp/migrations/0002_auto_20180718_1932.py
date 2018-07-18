# Generated by Django 2.0.7 on 2018-07-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='id',
        ),
        migrations.AddField(
            model_name='address',
            name='id_address',
            field=models.IntegerField(db_index=True, default='', primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsletterrecipient',
            name='email',
            field=models.EmailField(blank=None, db_index=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='proximity',
            name='city',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
