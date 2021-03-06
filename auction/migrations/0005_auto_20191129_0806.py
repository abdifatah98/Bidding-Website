# Generated by Django 2.1 on 2019-11-29 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_auto_20191123_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='AuctionStart',
        ),
        migrations.AddField(
            model_name='accounts',
            name='dateofbirth',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='Image',
            field=models.ImageField(blank=True, upload_to='Items/'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='Stats',
            field=models.BooleanField(choices=[(True, 'Open'), (False, 'Close')], default=True),
        ),
    ]
