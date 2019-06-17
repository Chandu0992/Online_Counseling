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
    counselor_id = models.CharField(max_length=11,primary_key=True)
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
    hod_id = models.CharField(max_length=11,primary_key=True)
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

class Add_Academic(models.Model):
    student_id = models.CharField(max_length=11)
    sem = models.CharField(max_length=4)
    subject = models.CharField(max_length=50)
    mid1 = models.CharField(max_length=3)
    mid2 = models.CharField(max_length=3)
    internal = models.CharField(max_length=3)
    external = models.CharField(max_length=3)

    def __str__(self):
        return self.student_id+" "+self.sem

class Counselor_Record(models.Model):
    reg_no = models.CharField(max_length=11,primary_key=True)
    stu_name = models.CharField(max_length=50)
    mentor_name = models.CharField(max_length=50)
    s1_r1 = models.CharField(max_length=10)
    s1_m1 = models.CharField(max_length=300)
    s1_r2 = models.CharField(max_length=10)
    s1_m2 = models.CharField(max_length=300)
    s2_r1 = models.CharField(max_length=10)
    s2_m1 = models.CharField(max_length=300)
    s2_r2 = models.CharField(max_length=10)
    s2_m2 = models.CharField(max_length=300)
    s3_r1 = models.CharField(max_length=10)
    s3_m1 = models.CharField(max_length=300)
    s3_r2 = models.CharField(max_length=10)
    s3_m2 = models.CharField(max_length=300)
    s4_r1 = models.CharField(max_length=10)
    s4_m1 = models.CharField(max_length=300)
    s4_r2 = models.CharField(max_length=10)
    s4_m2 = models.CharField(max_length=300)
    s5_r1 = models.CharField(max_length=10)
    s5_m1 = models.CharField(max_length=300)
    s5_r2 = models.CharField(max_length=10)
    s5_m2 = models.CharField(max_length=300)
    s6_r1 = models.CharField(max_length=10)
    s6_m1 = models.CharField(max_length=300)
    s6_r2 = models.CharField(max_length=10)
    s6_m2 = models.CharField(max_length=300)
    over_all_remarks = models.CharField(max_length=300,default='Good')

    def __str__(self):
        return self.reg_no+" "+self.over_all_remarks

class Discipline(models.Model):
    stu_id = models.CharField(max_length=11,primary_key=True)
    cou_id = models.CharField(max_length=11)

    gd1 = models.CharField(max_length=2)
    gd2 = models.CharField(max_length=2)
    gd3 = models.CharField(max_length=2)
    gd4 = models.CharField(max_length=2)
    gd5 = models.CharField(max_length=2)
    gd6 = models.CharField(max_length=2)

    cs1 = models.CharField(max_length=2)
    cs2 = models.CharField(max_length=2)
    cs3 = models.CharField(max_length=2)
    cs4 = models.CharField(max_length=2)
    cs5 = models.CharField(max_length=2)
    cs6 = models.CharField(max_length=2)

    gg1 = models.CharField(max_length=2)
    gg2 = models.CharField(max_length=2)
    gg3 = models.CharField(max_length=2)
    gg4 = models.CharField(max_length=2)
    gg5 = models.CharField(max_length=2)
    gg6 = models.CharField(max_length=2)

    bwp1 = models.CharField(max_length=2)
    bwp2 = models.CharField(max_length=2)
    bwp3 = models.CharField(max_length=2)
    bwp4 = models.CharField(max_length=2)
    bwp5 = models.CharField(max_length=2)
    bwp6 = models.CharField(max_length=2)

    bwf1 = models.CharField(max_length=2)
    bwf2 = models.CharField(max_length=2)
    bwf3 = models.CharField(max_length=2)
    bwf4 = models.CharField(max_length=2)
    bwf5 = models.CharField(max_length=2)
    bwf6 = models.CharField(max_length=2)

    cca1 = models.CharField(max_length=2)
    cca2 = models.CharField(max_length=2)
    cca3 = models.CharField(max_length=2)
    cca4 = models.CharField(max_length=2)
    cca5 = models.CharField(max_length=2)
    cca6 = models.CharField(max_length=2)

    ea1 = models.CharField(max_length=2)
    ea2 = models.CharField(max_length=2)
    ea3 = models.CharField(max_length=2)
    ea4 = models.CharField(max_length=2)
    ea5 = models.CharField(max_length=2)
    ea6 = models.CharField(max_length=2)

    bh1 = models.CharField(max_length=2)
    bh2 = models.CharField(max_length=2)
    bh3 = models.CharField(max_length=2)
    bh4 = models.CharField(max_length=2)
    bh5 = models.CharField(max_length=2)
    bh6 = models.CharField(max_length=2)

    og1 = models.CharField(max_length=2)
    og2 = models.CharField(max_length=2)
    og3 = models.CharField(max_length=2)
    og4 = models.CharField(max_length=2)
    og5 = models.CharField(max_length=2)
    og6 = models.CharField(max_length=2)

    da1 = models.CharField(max_length=2)
    da2 = models.CharField(max_length=2)
    da3 = models.CharField(max_length=2)
    da4 = models.CharField(max_length=2)
    da5 = models.CharField(max_length=2)
    da6 = models.CharField(max_length=2)

    is1 = models.CharField(max_length=2)
    is2 = models.CharField(max_length=2)
    is3 = models.CharField(max_length=2)
    is4 = models.CharField(max_length=2)
    is5 = models.CharField(max_length=2)
    is6 = models.CharField(max_length=2)

    im1 = models.CharField(max_length=2)
    im2 = models.CharField(max_length=2)
    im3 = models.CharField(max_length=2)
    im4 = models.CharField(max_length=2)
    im5 = models.CharField(max_length=2)
    im6 = models.CharField(max_length=2)

    rm1 = models.CharField(max_length=2)
    rm2 = models.CharField(max_length=2)
    rm3 = models.CharField(max_length=2)
    rm4 = models.CharField(max_length=2)
    rm5 = models.CharField(max_length=2)
    rm6 = models.CharField(max_length=2)

    empty1 = models.CharField(max_length=2)
    empty2 = models.CharField(max_length=2)
    empty3 = models.CharField(max_length=2)
    empty4 = models.CharField(max_length=2)
    empty5 = models.CharField(max_length=2)
    empty6 = models.CharField(max_length=2)

    place1 = models.CharField(max_length=20)
    gate1 = models.CharField(max_length=20)
    other1 = models.CharField(max_length=20)

    def __str__(self):
        return self.stu_id