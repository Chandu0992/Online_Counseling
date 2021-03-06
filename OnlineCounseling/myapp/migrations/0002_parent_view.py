# Generated by Django 2.2 on 2019-05-01 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent_View',
            fields=[
                ('student_id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('student_avg_academic', models.CharField(max_length=3)),
                ('student_lab_performance', models.CharField(max_length=3)),
                ('student_avg_attendance', models.CharField(max_length=3)),
                ('student_avg_curricular_activities', models.CharField(max_length=3)),
                ('student_sports', models.CharField(max_length=3)),
                ('student_project_performance', models.CharField(max_length=3)),
                ('student_over_all_performance', models.CharField(max_length=3)),
            ],
        ),
    ]
