from django.db import models

# Create your models here.
class Student_Registration(models.Model):
    registration_number = models.CharField(max_length=11,primary_key=True)
    student_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=5)
    year = models.CharField(max_length=1)
    semester = models.CharField(max_length=1)
    mobile_no = models.CharField(max_length=10)
    email_id = models.EmailField()
    admit_under = models.CharField(max_length=19)
    caste = models.CharField(max_length=15)
    icet_rank = models.CharField(max_length=5)
    date_of_birth = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=3)
    tenth_marks = models.CharField(max_length=3)
    percentage = models.CharField(max_length=3)
    name_of_parent = models.CharField(max_length=50)
    resident_address = models.CharField(max_length=500)
    occupation = models.CharField(max_length=30)
    parent_mobile_number = models.CharField(max_length=10)
    local_guardian = models.CharField(max_length=50,default=None)
    current_address = models.CharField(max_length=500,default=None)
    guardian_mobile_number = models.CharField(max_length=10,default=None)
    hobbies = models.CharField(max_length=50)
    games = models.CharField(max_length=30)
    literacy_activities = models.CharField(max_length=30)
    technical_activities = models.CharField(max_length=30)
    profile_pic = models.CharField(max_length=70,default='unknown.jpg')


    def __str__(self):
        return self.registration_number

class Counselor(models.Model):
    counselor_id = models.CharField(max_length=11)
    counselor_name = models.CharField(max_length=50)
    counselor_designation = models.CharField(max_length=50)
    counselor_pwd = models.CharField(max_length=250)

    def __str__(self):
        return self.counselor_id

class Add_Student(models.Model):
    counselor_id = models.CharField(max_length=11)
    student_id = models.CharField(max_length=11,primary_key=True)

    def __str__(self):
        return self.student_id

class Feed_Back(models.Model):
    reg_id = models.CharField(max_length=11,primary_key=True)
    question_1 = models.CharField(max_length=15)
    question_2 = models.CharField(max_length=15)
    question_3 = models.CharField(max_length=15)
    question_4 = models.CharField(max_length=15)
    question_5 = models.CharField(max_length=15)
    question_6 = models.CharField(max_length=15)
    question_7 = models.CharField(max_length=15)
    question_8 = models.CharField(max_length=15)
    question_9 = models.CharField(max_length=15)
    question_10 = models.CharField(max_length=15)
    question_11 = models.CharField(max_length=15)
    question_12 = models.CharField(max_length=15)
    question_13 = models.CharField(max_length=15)
    question_14 = models.CharField(max_length=15)
    question_15 = models.CharField(max_length=15)


    def __str__(self):
        return self.reg_id

class pro_Question(models.Model):
    id = models.AutoField(primary_key=True)
    counselor_id = models.CharField(max_length=11)
    student_id = models.CharField(max_length=11)
    pro_Question = models.CharField(max_length=200)
    stu_ans = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.student_id+' '+self.pro_Question

class Student_Question(models.Model):
    id = models.AutoField(primary_key=True)
    counselor_id = models.CharField(max_length=11)
    student_id = models.CharField(max_length=11)
    stu_Question = models.CharField(max_length=200)
    pro_ans = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.counselor_id+' '+self.stu_Question

class HOD(models.Model):
    hod_id = models.CharField(max_length=11)
    hod_name = models.CharField(max_length=50)
    hod_designation = models.CharField(max_length=50)
    hod_pwd = models.CharField(max_length=250)

    def __str__(self):
        return self.hod_id

class Parent_View(models.Model):
    student_id = models.CharField(max_length=11,primary_key=True)
    student_avg_academic = models.CharField(max_length=3)
    student_lab_performance = models.CharField(max_length=3)
    student_avg_attendance = models.CharField(max_length=3)
    student_avg_curricular_activities = models.CharField(max_length=3)
    student_sports = models.CharField(max_length=3)
    student_project_performance = models.CharField(max_length=3)
    student_over_all_performance = models.CharField(max_length=3)

    def __str__(self):
        return self.student_id