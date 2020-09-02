# Generated by Django 2.1 on 2019-11-23 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auction_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='AuctionEnd',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='auction',
            name='AuctionStart',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='auction',
            name='HighestBidder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
