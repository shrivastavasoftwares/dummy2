# Generated by Django 2.2.5 on 2021-01-20 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('larave_appl', '0010_auto_20210119_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bank_id', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('Bank_name', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee_info',
            name='Bank_name',
        ),
        migrations.AddField(
            model_name='employee_info',
            name='Bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='larave_appl.Bank'),
        ),
    ]
