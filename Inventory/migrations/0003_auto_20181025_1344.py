# Generated by Django 2.0.5 on 2018-10-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_auto_20181025_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='desk',
            name='Odd_Main_Depth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='desk',
            name='Odd_Side_Depth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='desk',
            name='Main_Depth',
            field=models.IntegerField(choices=[(400, '400'), (450, '450'), (500, '500'), (600, '600'), (650, '650'), (700, '700'), (750, '750'), (800, '800'), (850, '850'), (900, '900'), (1100, '1100'), (1200, '1200'), (1350, '1350'), (1400, '1400'), (1450, '1450'), (1500, '1500'), (1600, '1600'), (1650, '1650'), (1700, '1700'), (1800, '1800'), (2100, '2100'), (-1, 'Other Measurements')], default=600),
        ),
        migrations.AlterField(
            model_name='desk',
            name='Side_Depth',
            field=models.IntegerField(choices=[(400, '400'), (450, '450'), (500, '500'), (600, '600'), (650, '650'), (700, '700'), (750, '750'), (800, '800'), (850, '850'), (900, '900'), (1100, '1100'), (1200, '1200'), (1350, '1350'), (1400, '1400'), (1450, '1450'), (1500, '1500'), (1600, '1600'), (1650, '1650'), (1700, '1700'), (1800, '1800'), (2100, '2100'), (-1, 'Other Measurements')], default=600),
        ),
    ]
