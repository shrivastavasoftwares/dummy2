# Generated by Django 2.2.5 on 2021-01-25 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('larave_appl', '0011_auto_20210120_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='District_State',
        ),
        migrations.RemoveField(
            model_name='district',
            name='District_city',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='District',
        ),
    ]
