# Generated by Django 2.2.1 on 2019-06-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_counselor_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='counselor_record',
            name='over_all_remarks',
            field=models.CharField(default='Good', max_length=300),
        ),
    ]