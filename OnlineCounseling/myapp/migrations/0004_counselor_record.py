# Generated by Django 2.2.1 on 2019-06-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_add_academic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counselor_Record',
            fields=[
                ('reg_no', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=50)),
                ('mentor_name', models.CharField(max_length=50)),
                ('s1_r1', models.CharField(max_length=10)),
                ('s1_m1', models.CharField(max_length=300)),
                ('s1_r2', models.CharField(max_length=10)),
                ('s1_m2', models.CharField(max_length=300)),
                ('s2_r1', models.CharField(max_length=10)),
                ('s2_m1', models.CharField(max_length=300)),
                ('s2_r2', models.CharField(max_length=10)),
                ('s2_m2', models.CharField(max_length=300)),
                ('s3_r1', models.CharField(max_length=10)),
                ('s3_m1', models.CharField(max_length=300)),
                ('s3_r2', models.CharField(max_length=10)),
                ('s3_m2', models.CharField(max_length=300)),
                ('s4_r1', models.CharField(max_length=10)),
                ('s4_m1', models.CharField(max_length=300)),
                ('s4_r2', models.CharField(max_length=10)),
                ('s4_m2', models.CharField(max_length=300)),
                ('s5_r1', models.CharField(max_length=10)),
                ('s5_m1', models.CharField(max_length=300)),
                ('s5_r2', models.CharField(max_length=10)),
                ('s5_m2', models.CharField(max_length=300)),
                ('s6_r1', models.CharField(max_length=10)),
                ('s6_m1', models.CharField(max_length=300)),
                ('s6_r2', models.CharField(max_length=10)),
                ('s6_m2', models.CharField(max_length=300)),
            ],
        ),
    ]
