# Generated by Django 2.2 on 2019-05-01 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Student',
            fields=[
                ('counselor_id', models.CharField(max_length=11)),
                ('student_id', models.CharField(max_length=11, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Counselor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counselor_id', models.CharField(max_length=11)),
                ('counselor_name', models.CharField(max_length=50)),
                ('counselor_designation', models.CharField(max_length=50)),
                ('counselor_pwd', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Feed_Back',
            fields=[
                ('reg_id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('question_1', models.CharField(max_length=15)),
                ('question_2', models.CharField(max_length=15)),
                ('question_3', models.CharField(max_length=15)),
                ('question_4', models.CharField(max_length=15)),
                ('question_5', models.CharField(max_length=15)),
                ('question_6', models.CharField(max_length=15)),
                ('question_7', models.CharField(max_length=15)),
                ('question_8', models.CharField(max_length=15)),
                ('question_9', models.CharField(max_length=15)),
                ('question_10', models.CharField(max_length=15)),
                ('question_11', models.CharField(max_length=15)),
                ('question_12', models.CharField(max_length=15)),
                ('question_13', models.CharField(max_length=15)),
                ('question_14', models.CharField(max_length=15)),
                ('question_15', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hod_id', models.CharField(max_length=11)),
                ('hod_name', models.CharField(max_length=50)),
                ('hod_designation', models.CharField(max_length=50)),
                ('hod_pwd', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='pro_Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('counselor_id', models.CharField(max_length=11)),
                ('student_id', models.CharField(max_length=11)),
                ('pro_Question', models.CharField(max_length=200)),
                ('stu_ans', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('counselor_id', models.CharField(max_length=11)),
                ('student_id', models.CharField(max_length=11)),
                ('stu_Question', models.CharField(max_length=200)),
                ('pro_ans', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Registration',
            fields=[
                ('registration_number', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=5)),
                ('year', models.CharField(max_length=1)),
                ('semester', models.CharField(max_length=1)),
                ('mobile_no', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=254)),
                ('admit_under', models.CharField(max_length=19)),
                ('caste', models.CharField(max_length=15)),
                ('icet_rank', models.CharField(max_length=5)),
                ('date_of_birth', models.CharField(max_length=10)),
                ('blood_group', models.CharField(max_length=3)),
                ('tenth_marks', models.CharField(max_length=3)),
                ('percentage', models.CharField(max_length=3)),
                ('name_of_parent', models.CharField(max_length=50)),
                ('resident_address', models.CharField(max_length=500)),
                ('occupation', models.CharField(max_length=30)),
                ('parent_mobile_number', models.CharField(max_length=10)),
                ('local_guardian', models.CharField(default=None, max_length=50)),
                ('current_address', models.CharField(default=None, max_length=500)),
                ('guardian_mobile_number', models.CharField(default=None, max_length=10)),
                ('hobbies', models.CharField(max_length=50)),
                ('games', models.CharField(max_length=30)),
                ('literacy_activities', models.CharField(max_length=30)),
                ('technical_activities', models.CharField(max_length=30)),
                ('profile_pic', models.CharField(default='unknown.jpg', max_length=70)),
            ],
        ),
    ]
