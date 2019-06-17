from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import Student_Registration,Counselor,Student_Question,Counselor_Record
from .models import HOD,Add_Student,Feed_Back,pro_Question,Parent_View,Add_Academic,Discipline
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
import random

def myotp():
    otp = random.SystemRandom().randint(100000, 99999999)
    return str(otp)
otp = myotp()
#Email Imports
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.
def showIndex(request,msg=None):
    return render(request,'myapp/Home_Page.html',{'msg':msg})

def Register_Student(request):
    registration_number = request.POST.get('reg_no')
    student_name = request.POST.get('student_name')
    branch = request.POST.get('branch')
    year = request.POST.get('year')
    semester = request.POST.get('semester')
    mobile_no = request.POST.get('mob_no')
    email_id = request.POST.get('email_id')
    admit_under = request.POST.get('admit_under')
    caste =request.POST.get('caste')
    icet_rank = request.POST.get('icet_rank')
    date_of_birth = request.POST.get('dob')
    blood_group = request.POST.get('blood_group')
    tenth_marks = request.POST.get('ssc_marks')
    percentage = request.POST.get('ssc_per')
    name_of_parent = request.POST.get('parent_name')
    resident_address = request.POST.get('home_address')
    occupation = request.POST.get('occupation')
    parent_mobile_number = request.POST.get('p_mob_no')
    local_guardian = request.POST.get('local_guardian')
    current_address = request.POST.get('guard_address')
    guardian_mobile_number = request.POST.get('g_mob_no')
    hobbies = request.POST.get('hobbies')
    games = request.POST.get('games')
    literacy_activities = request.POST.get('lit_activity')
    technical_activities = request.POST.get('tech_activity')
    reg = Student_Registration(
        registration_number=registration_number,student_name=student_name,
        semester=semester,branch=branch,year=year,mobile_no=mobile_no,email_id=email_id,admit_under=admit_under,
        caste=caste,icet_rank=icet_rank,date_of_birth=date_of_birth,blood_group=blood_group,
        tenth_marks=tenth_marks,percentage=percentage,name_of_parent=name_of_parent,
        resident_address=resident_address,occupation=occupation,parent_mobile_number=parent_mobile_number,
        local_guardian=local_guardian,current_address=current_address,guardian_mobile_number=guardian_mobile_number,
        hobbies=hobbies,games=games,literacy_activities=literacy_activities,technical_activities=technical_activities
    )
    reg.save()
    return showIndex(request,msg="Registered Success...")

def show_counselor(request,msg=None):
    return render(request,'myapp/counselor.html',{'msg':msg})

def reg_counselor(request):
    cou_id = request.POST.get('counselor_id')
    cou_name = request.POST.get('counselor_name')
    cou_desig = request.POST.get('counselor_designation')
    cou_pwd = request.POST.get('counselor_password')
    hash_pwd = make_password(cou_pwd)
    res = Counselor(counselor_designation=cou_desig,counselor_id=cou_id,counselor_name=cou_name,counselor_pwd=hash_pwd)
    res.save()
    print("Counselor with {} is Registered !".format(cou_id))
    return show_counselor(request,msg="Registered Successfully !")

def fetch_counselor(request,res=None,reg_id=None,student=None):
    my_counselor = Counselor.objects.filter(counselor_id=request.session.get('cou_id'))
    cou_name = list(my_counselor)[0]
    cou_name = cou_name.counselor_name
    res_student = Add_Student.objects.filter(counselor_id=request.session.get('cou_id'))
    res_student = list(res_student)
    return render(request,'myapp/counselor_home.html',{'cou_name':cou_name,'res_student': res_student,'res':res,'reg_id':reg_id,'student':student})


def login_counselor(request):
    cou_id = request.POST.get('counselor_id')
    cou_pwd = request.POST.get('counselor_pwd')
    res = Counselor.objects.filter(counselor_id=cou_id)
    print(res)
    if len(res) == 0:
        return show_counselor(request)
    else:
        res1 = list(res)[0]
        if check_password(cou_pwd,res1.counselor_pwd):
            request.session['cou_id'] = cou_id
            return fetch_counselor(request)
        else:
            return show_counselor(request)

def addStudent(request):
    cou_id = request.session.get('cou_id')
    stu_id = request.POST['student_id']
    res = Add_Student(counselor_id=cou_id,student_id=stu_id)
    res.save()
    print("Student Added to Counselor")
    # Modification needed for counselor login
    return fetch_counselor(request,None,None)

def show_feed_back(request):
    #reg_id = request.session.get('stu_id')
    reg_id = request.POST.get('stu_id')
    my_feed_back = Feed_Back.objects.filter(reg_id=reg_id)
    if len(my_feed_back) == 1:
        return render(request, 'myapp/feed_back.html',
                      {'my_feed_back': 'Feed back already given thankyou for the Intrest!'})
    else:
        return render(request, 'myapp/feed_back.html')

def get_feed_back(request):
    reg_id = request.session.get('stu_id')
    que_1 = request.POST.get('q1')
    que_2 = request.POST.get('q2')
    que_3 = request.POST.get('q3')
    que_4 = request.POST.get('q4')
    que_5 = request.POST.get('q5')
    que_6 = request.POST.get('q6')
    que_7 = request.POST.get('q7')
    que_8 = request.POST.get('q8')
    que_9 = request.POST.get('q9')
    que_10 = request.POST.get('q10')
    que_11 = request.POST.get('q11')
    que_12 = request.POST.get('q12')
    que_13 = request.POST.get('q13')
    que_14 = request.POST.get('q14')
    que_15 = request.POST.get('q15')

    res = Feed_Back(reg_id=reg_id,question_1=que_1,question_2=que_2,question_3=que_3,question_4=que_4,
                    question_5=que_5,question_6=que_6,question_7=que_7,question_8=que_8,question_9=que_9,
                    question_10=que_10,question_11=que_11,question_12=que_12,question_13=que_13,
                    question_14=que_14,question_15=que_15)
    res.save()
    return render(request,'myapp/feed_back.html',{'my_feed_back':'Feed back Given Success!'})

def view_feed_back(request):

    if request.method == 'POST':
        reg_id = request.POST.get('student_id')
        res = Feed_Back.objects.filter(reg_id=reg_id)
        if len(res) == 0:
            return fetch_counselor(request, res, reg_id)
        else:
            res = list(res)[0]
            return fetch_counselor(request,res,reg_id)
    else:
        reg_id = request.session.get('stu_id')
        res = Feed_Back.objects.filter(reg_id=reg_id)
        if len(res) == 0:
            return render(request, 'myapp/student_home.html', {'fed_msg': "Feed Back Not Given..."})
        else:
            res = list(res)[0]
            return render(request, 'myapp/student_home.html', {'fed_res': res})


def view_feed_back_hod(request):
    reg_id = request.POST.get('student_id')
    res = Feed_Back.objects.filter(reg_id=reg_id)
    if len(res) == 0:
        return fetch_hod(request,res,reg_id)
    else:
        res = list(res)[0]
        return fetch_hod(request,res,reg_id)

def view_student(request):
    reg_id = request.POST.get('student_id')
    student = Student_Registration.objects.filter(registration_number=reg_id)
    student = list(student)[0]
    return fetch_counselor(request,res=None,reg_id=None,student=student)

def view_student_hod(request):
    reg_id = request.POST.get('student_id')
    student = Student_Registration.objects.filter(registration_number=reg_id)
    student = list(student)[0]
    return fetch_hod(request,res=None,reg_id=None,student=student)


def show_ask_question(request):
    my_counselor = Counselor.objects.filter(counselor_id=request.session.get('cou_id'))
    cou_name = list(my_counselor)[0]
    cou_name = cou_name.counselor_name
    student_id = request.POST.get('student_id')
    request.session['stu_id'] = student_id
    return render(request, 'myapp/counselor_ask_question.html',{'cou_name':cou_name})

def get_Question(request):
    student_id = request.session.get('stu_id')
    counselor_id = request.session.get('cou_id')
    pro_que = request.POST.get('pro_question')
    res = pro_Question(counselor_id=counselor_id,student_id=student_id,pro_Question=pro_que)
    res.save()
    return fetch_counselor(request)

def show_ask_question_hod(request):
    hod_name = HOD.objects.filter(hod_id=request.session.get('hod_id'))
    hod_name = list(hod_name)[0]
    hod_name = hod_name.hod_name
    student_id = request.POST.get('student_id')
    request.session['stu_id'] = student_id
    return render(request, 'myapp/hod_ask_question.html',{'hod_name':hod_name})

def get_Question_hod(request):
    student_id = request.session.get('stu_id')
    counselor_id = request.session.get('hod_id')
    pro_que = request.POST.get('pro_question')
    res = pro_Question(counselor_id=counselor_id,student_id=student_id,pro_Question=pro_que)
    res.save()
    return fetch_hod(request)


def student_Login(request,msg=None):
    return render(request,'myapp/student_login.html',{'login_msg':msg})

def student_login_verification(request):

    reg_id = request.POST.get('reg_id')
    res = Student_Registration.objects.filter(registration_number=reg_id)
    if len(res) == 0:
        return student_Login(request,msg="Registered Id is not valid Please Register..!")
    res = list(res)[0]
    email_id = res.email_id

    sub = "Your Login Otp For Online Counseling...!"
    message = "Please Use this otp to login : "+otp
    print(message)
    #to_email = 'crazyboy_suggestions@protonmail.com'

    from_user = settings.EMAIL_HOST_USER
    to_user = email_id
    password = settings.EMAIL_HOST_PASSWORD

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_user, password)

    subject = sub

    msg = MIMEMultipart()
    msg['From'] = from_user
    msg['To'] = to_user
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))

    text = msg.as_string()
    server.sendmail(from_user, to_user, text)

    server.close()

    request.session['stu_id'] = reg_id
    return render(request,'myapp/otp_verification.html')

def student_login_confirmation(request):

    my_otp = request.POST.get('std_otp')

    if otp == my_otp:
        res = Student_Registration.objects.filter(registration_number=request.session.get('stu_id'))
        res = list(res)[0]
        return render(request,'myapp/student_home.html',{'res':res})
    else:
        return student_Login(request)

def student_home(request):
    res = Student_Registration.objects.filter(registration_number=request.session.get('stu_id'))
    res = list(res)[0]
    return render(request, 'myapp/student_home.html', {'res': res})


def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['my_pic']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        print(uploaded_file.name, '  ', uploaded_file.size)
        #stu_id  = request.session.get('stu_id')
        Student_Registration.objects.filter(registration_number=request.session.get('stu_id')).update(profile_pic=uploaded_file.name)
        res = Student_Registration.objects.filter(registration_number=request.session.get('stu_id'))
        res = list(res)[0]
    return render(request, 'myapp/student_home.html', {'res': res})

def show_student_Questions(request):
    stu_id = request.session.get('stu_id')
    student_question = Add_Student.objects.filter(student_id=stu_id)
    if len(student_question) == 0:
        return render(request, "myapp/student_home.html", {'student_question_res': "You are not assign to any Counselor Contact Admin or Hod."})
    else:
        return render(request, "myapp/student_ask_question.html")



def student_Questions(request):
    stu_Que = request.POST.get('std_que')
    stu_id = request.session.get('stu_id')

    student_question = Add_Student.objects.filter(student_id=stu_id)
    student_question = list(student_question)[0]
    pro_id = student_question.counselor_id
    std_question = Student_Question(counselor_id=pro_id,student_id=stu_id,stu_Question=stu_Que,pro_ans='')
    std_question.save()
    return render(request, "myapp/student_ask_question.html",{'student_question_res': "Question Asked Sucessfully !"})

def Student_Logout(request):
    del request.session['stu_id']
    try:
        del request.session['stu_msg_id']
        del request.session['hod_msg_id']
        del request.session['cou_msg_id']
    except KeyError:
        return student_Login(request)
    return student_Login(request)

def Counselor_Logout(request):
    try:
        if request.session['cou_id']:
            del request.session['cou_id']
            try:
                del request.session['stu_msg_id']
                del request.session['hod_msg_id']
                del request.session['cou_msg_id']
            except KeyError:
                return show_counselor(request)
            return show_counselor(request,msg = 'Logout Successfully')
    except KeyError:
        return show_counselor(request, msg="Please Login First!")

def Hod_Logout(request):
    try:
        if request.session['hod_id']:
            del request.session['hod_id']
            try:
                del request.session['stu_msg_id']
                del request.session['hod_msg_id']
                del request.session['cou_msg_id']
            except KeyError:
                return show_hod(request)
            return show_hod(request,msg = 'Logout Successfully')
    except KeyError:
        return show_hod(request, msg="Please Login First!")


def show_pro_que(request):
    pro_ques_res = pro_Question.objects.filter(student_id=request.session.get('stu_id'))
    pro_ques_res = list(pro_ques_res)
    if len(pro_ques_res) == 0:
        return render(request,'myapp/student_ask_question.html',{'pro_ques_msg':"No Questions was asked by your Counselor..!"})
    else:
        return render(request,'myapp/student_ask_question.html',{'pro_ques_res':pro_ques_res})


def ans_to_counselor(request):
    q_id = request.POST.get('my_id')
    stu_ans = request.POST.get('my_ans')
    #Student_Registration.objects.filter(registration_number=request.session.get('stu_id')).update(profile_pic=uploaded_file.name)
    pro_Question.objects.filter(id=q_id).update(stu_ans=stu_ans)
    return show_pro_que(request)

def ans_to_student(request):
    q_id = request.POST.get('my_id')
    pro_ans = request.POST.get('my_ans')
    #Student_Registration.objects.filter(registration_number=request.session.get('stu_id')).update(profile_pic=uploaded_file.name)
    Student_Question.objects.filter(id=q_id).update(pro_ans=pro_ans)
    return show_stu_que(request)

def show_stu_que(request):
    my_counselor = Counselor.objects.filter(counselor_id=request.session.get('cou_id'))
    cou_name = list(my_counselor)[0]
    cou_name = cou_name.counselor_name
    stu_ques_res = Student_Question.objects.filter(counselor_id=request.session.get('cou_id'),student_id=request.session.get('stu_id'))
    stu_ques_res = list(stu_ques_res)
    if len(stu_ques_res) == 0:
        return render(request, 'myapp/counselor_ask_question.html',
                      {'cou_name':cou_name,'stu_ques_msg': "No Questions was asked by your Student..!"})
    else:
        return render(request, 'myapp/counselor_ask_question.html', {'cou_name':cou_name,'stu_ques_res': stu_ques_res})

def show_stu_que_hod(request):
    hod_name = HOD.objects.filter(hod_id=request.session.get('hod_id'))
    hod_name = list(hod_name)[0]
    hod_name = hod_name.hod_name
    stu_ques_res = Student_Question.objects.filter(counselor_id=request.session.get('hod_id'),student_id=request.session.get('stu_id'))
    stu_ques_res = list(stu_ques_res)
    if len(stu_ques_res) == 0:
        return render(request, 'myapp/hod_ask_question.html',
                      {'hod_name':hod_name,'stu_ques_msg': "No Questions was asked by your Student..!"})
    else:
        return render(request, 'myapp/hod_ask_question.html', {'hod_name':hod_name,'stu_ques_res': stu_ques_res})


def Show_Register_Student(request):
    return render(request,'myapp/index.html')

def show_hod(request,msg=None):
    return render(request,'myapp/hod.html',{'msg':msg})


def reg_hod(request):
    hod_id = request.POST.get('hod_id')
    hod_name = request.POST.get('hod_name')
    hod_desig = request.POST.get('hod_designation')
    hod_pwd = request.POST.get('hod_password')
    hash_pwd = make_password(hod_pwd)
    res = HOD(hod_designation=hod_desig, hod_id=hod_id, hod_name=hod_name,hod_pwd=hash_pwd)
    res.save()
    return show_hod(request,msg="Registered Successfully !")


def addStudent_hod(request):
    cou_id = request.session.get('hod_id')
    stu_id = request.POST['student_id']
    res = Add_Student(counselor_id=cou_id,student_id=stu_id)
    res.save()
    return fetch_hod(request,None,None)


def fetch_hod(request,res=None,reg_id=None,student=None):
    hod_name = HOD.objects.filter(hod_id=request.session.get('hod_id'))
    hod_name = list(hod_name)[0]
    hod_name = hod_name.hod_name
    res_student = Add_Student.objects.filter(counselor_id=request.session.get('hod_id'))
    res_student = list(res_student)
    return render(request,'myapp/hod_home.html',{'hod_name':hod_name,'res_student': res_student,'res':res,'reg_id':reg_id,'student':student})

def show_student_performance(request,msg=None):
    return render(request,'myapp/add_student_performance.html',{'msg':msg})

def add_performance(request):
    student_id = request.POST.get('student_id')
    student_avg_academic = request.POST.get('student_avg_academic')
    student_lab_performance = request.POST.get('student_lab_performance')
    student_avg_attendance = request.POST.get('student_avg_attendance')
    student_avg_curricular_activities = request.POST.get('student_avg_curricular_activities')
    student_sports = request.POST.get('student_sports')
    student_over_all_performance = request.POST.get('student_over_all_performance')
    student_project_performance = request.POST.get('student_project_performance')

    std_performance = Parent_View(student_id=student_id,student_avg_academic=student_avg_academic,
                                  student_lab_performance=student_lab_performance,
                                  student_avg_attendance=student_avg_attendance,
                                  student_avg_curricular_activities=student_avg_curricular_activities,
                                  student_sports=student_sports,
                                  student_over_all_performance=student_over_all_performance,
                                  student_project_performance=student_project_performance)
    std_performance.save()
    return show_student_performance(request,"Performance Added Successfully")

def login_hod(request):
    hod_id = request.POST.get('hod_id')
    hod_pwd = request.POST.get('hod_pwd')
    res = HOD.objects.filter(hod_id=hod_id)
    if len(res) == 0:
        return show_hod(request)
    else:
        res1 = list(res)[0]
        if check_password(hod_pwd, res1.hod_pwd):
            request.session['hod_id'] = hod_id
            return fetch_hod(request)
        else:
            return show_hod(request)

def show_feedback_all_students(request):
    #hod_id = request.session.get('hod_id')
    review_all = Feed_Back.objects.all()
    return render(request,'myapp/review.html',{'review_all':review_all})


def show_parent(request):
    return render(request,'myapp/parent_view.html')


def show_student_list(request):
    branch = request.POST.get('branch')
    year = request.POST.get('year')
    sem = request.POST.get('semester')
    reg_nums = Student_Registration.objects.filter(branch=branch,year=year,semester=sem)
    reg_nums = list(reg_nums)
    return render(request,'myapp/parent_view.html',{'reg_nums':reg_nums})


def show_my_graph(request):
    reg_num = request.POST.get('student_id')
    stu_per = Parent_View.objects.filter(student_id=reg_num)
    if len(stu_per) == 0:
        return render(request, 'myapp/parent_view.html',{'stu_msg':'Invalid Selection of the above menu or Search not found'})
    else:
        stu_per = list(stu_per)
        my_val = []
        for student in stu_per:
            my_val.append(int(student.student_avg_academic))
            my_val.append(int(student.student_lab_performance))
            my_val.append(int(student.student_avg_attendance))
            my_val.append(int(student.student_avg_curricular_activities))
            my_val.append(int(student.student_sports))
            my_val.append(int(student.student_project_performance))
            my_val.append(int(student.student_over_all_performance))

        return render(request, 'myapp/parent_view.html',{'stu_per':my_val})

def show_academic_year(request):
    cou_id = request.session.get('cou_id')
    my_stu_lst = Add_Student.objects.filter(counselor_id=cou_id)
    my_stu_lst = list(my_stu_lst)
    return render(request,"myapp/academic_year_input.html",{'my_stu_lst':my_stu_lst})

def add_academic_year(request):
    stu_id = request.POST.get('reg_no')
    sem = request.POST.get('sem')
    subject = request.POST.get('course_name')
    mid1 = request.POST.get('mid1')
    mid2 = request.POST.get('mid2')
    _int = request.POST.get('internal')
    _ext = request.POST.get('external')
    my_marks = Add_Academic(student_id=stu_id,sem=sem,subject=subject,mid1=mid1,mid2=mid2,internal=_int,external=_ext)
    my_marks.save()
    return show_academic_year(request)

def Show_academic_year(request):
    cou_id = request.session.get('cou_id')
    my_stu_lst = Add_Student.objects.filter(counselor_id=cou_id)
    my_stu_lst = list(my_stu_lst)
    return render(request,"myapp/academic_year.html",{'my_stu_lst':my_stu_lst})

def fetch_Student_academic_detail(request):
    stu_id = request.POST.get('reg_id')
    sem = request.POST.get('sem')
    print(stu_id)
    print(sem)
    my_stu_details = Add_Academic.objects.filter(student_id=stu_id,sem=sem)
    my_stu_details = list(my_stu_details)
    for rec in my_stu_details:
        print(rec.subject)
        print(rec.mid1)
        print(rec.mid2)
        print(rec.internal)
        print(rec.external)
    return render(request,'myapp/academic_year.html',{'my_stu_details':my_stu_details,'sem':sem})

def show_counseling_record(request):
    return render(request,'myapp/counseling_record.html')

def counseling_record(request):

    reg_no = request.POST.get('stu_reg')
    stu_name = request.POST.get('stu_name')
    mentor_name = request.POST.get('stu_mentor')

    s1_r1 = request.POST.get('s1_r1')
    s1_m1 = request.POST.get('s1_m1')
    s1_r2 = request.POST.get('s1_r2')
    s1_m2 = request.POST.get('s1_m2')

    s2_r1 = request.POST.get('s2_r1')
    s2_m1 = request.POST.get('s2_m1')
    s2_r2 = request.POST.get('s2_r2')
    s2_m2 = request.POST.get('s2_m2')

    s3_r1 = request.POST.get('s3_r1')
    s3_m1 = request.POST.get('s3_m1')
    s3_r2 = request.POST.get('s3_r2')
    s3_m2 = request.POST.get('s3_m2')

    s4_r1 = request.POST.get('s4_r1')
    s4_m1 = request.POST.get('s4_m1')
    s4_r2 = request.POST.get('s4_r2')
    s4_m2 = request.POST.get('s4_m2')

    s5_r1 = request.POST.get('s5_r1')
    s5_m1 = request.POST.get('s5_m1')
    s5_r2 = request.POST.get('s5_r2')
    s5_m2 = request.POST.get('s5_m2')

    s6_r1 = request.POST.get('s6_r1')
    s6_m1 = request.POST.get('s6_m1')
    s6_r2 = request.POST.get('s6_r2')
    s6_m2 = request.POST.get('s6_m2')

    record = Counselor_Record(reg_no=reg_no,stu_name=stu_name,mentor_name=mentor_name,s1_r1=s1_r1,
                              s1_m1=s1_m1,s1_r2=s1_r2,s1_m2=s1_m2,s2_r1=s2_r1,s2_m1=s2_m1,s2_r2=s2_r2,
                              s2_m2=s2_m2,s3_r1=s3_r1,s3_m1=s3_m1,s3_r2=s3_r2,s3_m2=s3_m2,s4_r1=s4_r1,
                              s4_m1=s4_m1,s4_r2=s4_r2,s4_m2=s4_m2,s5_r1=s5_r1,s5_m1=s5_m1,s5_r2=s5_r2,
                              s5_m2=s5_m2,s6_r1=s6_r1,s6_m1=s6_m1,s6_r2=s6_r2,s6_m2=s6_m2)
    record.save()
    return show_counseling_record(request)

def show_fetch_counselor_record(request):
    return render(request,'myapp/show_counselor_record.html')

def fetch_counselor_record(request):
    student_id = request.POST.get('stu_id')
    my_record = Counselor_Record.objects.filter(reg_no=student_id)
    if len(my_record) == 0:
        return render(request,'myapp/show_counselor_record.html',{'msg':"Record Not found for Searched Registered Id "})
    else:
        my_record = list(my_record)[0]
        return render(request, 'myapp/show_counselor_record.html',{'my_record':my_record})

def show_discipline(required):
    return render(required,'myapp/Discipline.html')

def get_discipline(request):
    stu_id = request.POST.get('stu_id')
    cou_id = request.session.get('cou_id')

    gd1 = request.POST.get('gd1')
    gd2 = request.POST.get('gd2')
    gd3 = request.POST.get('gd3')
    gd4 = request.POST.get('gd4')
    gd5 = request.POST.get('gd5')
    gd6 = request.POST.get('gd6')

    cs1 = request.POST.get('cs1')
    cs2 = request.POST.get('cs2')
    cs3 = request.POST.get('cs3')
    cs4 = request.POST.get('cs4')
    cs5 = request.POST.get('cs5')
    cs6 = request.POST.get('cs6')

    gg1 = request.POST.get('gg1')
    gg2 = request.POST.get('gg2')
    gg3 = request.POST.get('gg3')
    gg4 = request.POST.get('gg4')
    gg5 = request.POST.get('gg5')
    gg6 = request.POST.get('gg6')

    bwp1 = request.POST.get('bwp1')
    bwp2 = request.POST.get('bwp2')
    bwp3 = request.POST.get('bwp3')
    bwp4 = request.POST.get('bwp4')
    bwp5 = request.POST.get('bwp5')
    bwp6 = request.POST.get('bwp6')

    bwf1 = request.POST.get('bwf1')
    bwf2 = request.POST.get('bwf2')
    bwf3 = request.POST.get('bwf3')
    bwf4 = request.POST.get('bwf4')
    bwf5 = request.POST.get('bwf5')
    bwf6 = request.POST.get('bwf6')

    cca1 = request.POST.get('cca1')
    cca2 = request.POST.get('cca2')
    cca3 = request.POST.get('cca3')
    cca4 = request.POST.get('cca4')
    cca5 = request.POST.get('cca5')
    cca6 = request.POST.get('cca6')

    ea1 = request.POST.get('ea1')
    ea2 = request.POST.get('ea2')
    ea3 = request.POST.get('ea3')
    ea4 = request.POST.get('ea4')
    ea5 = request.POST.get('ea5')
    ea6 = request.POST.get('ea6')

    bh1 = request.POST.get('bh1')
    bh2 = request.POST.get('bh2')
    bh3 = request.POST.get('bh3')
    bh4 = request.POST.get('bh4')
    bh5 = request.POST.get('bh5')
    bh6 = request.POST.get('bh6')

    og1 = request.POST.get('og1')
    og2 = request.POST.get('og2')
    og3 = request.POST.get('og3')
    og4 = request.POST.get('og4')
    og5 = request.POST.get('og5')
    og6 = request.POST.get('og6')

    da1 = request.POST.get('da1')
    da2 = request.POST.get('da2')
    da3 = request.POST.get('da3')
    da4 = request.POST.get('da4')
    da5 = request.POST.get('da5')
    da6 = request.POST.get('da6')

    is1 = request.POST.get('is1')
    is2 = request.POST.get('is2')
    is3 = request.POST.get('is3')
    is4 = request.POST.get('is4')
    is5 = request.POST.get('is5')
    is6 = request.POST.get('is6')

    im1 = request.POST.get('im1')
    im2 = request.POST.get('im2')
    im3 = request.POST.get('im3')
    im4 = request.POST.get('im4')
    im5 = request.POST.get('im5')
    im6 = request.POST.get('im6')

    rm1 = request.POST.get('rm1')
    rm2 = request.POST.get('rm2')
    rm3 = request.POST.get('rm3')
    rm4 = request.POST.get('rm4')
    rm5 = request.POST.get('rm5')
    rm6 = request.POST.get('rm6')

    empty1 = request.POST.get('empty1')
    empty2 = request.POST.get('empty2')
    empty3 = request.POST.get('empty3')
    empty4 = request.POST.get('empty4')
    empty5 = request.POST.get('empty5')
    empty6 = request.POST.get('empty6')

    place1 = request.POST.get('place1')
    gate1 = request.POST.get('gate1')
    other1 = request.POST.get('other1')

    disp = Discipline(stu_id=stu_id,cou_id=cou_id,gd1=gd1,gd2=gd2,gd3=gd3,gd4=gd4,gd5=gd5,gd6=gd6,
                      cs1=cs1,cs2=cs2,cs3=cs3,cs4=cs4,cs5=cs5,cs6=cs6,
                      gg1=gg1,gg2=gg2,gg3=gg3,gg4=gg4,gg5=gg5,gg6=gg6,
                      bwp1=bwp1,bwp2=bwp2,bwp3=bwp3,bwp4=bwp4,bwp5=bwp5,bwp6=bwp6,
                      bwf1=bwf1,bwf2=bwf2,bwf3=bwf3,bwf4=bwf4,bwf5=bwf5,bwf6=bwf6,
                      cca1=cca1,cca2=cca2,cca3=cca3,cca4=cca4,cca5=cca5,cca6=cca6,
                      ea1=ea1,ea2=ea2,ea3=ea3,ea4=ea4,ea5=ea5,ea6=ea6,
                      bh1=bh1,bh2=bh2,bh3=bh3,bh4=bh4,bh5=bh5,bh6=bh6,
                      og1=og1,og2=og2,og3=og3,og4=og4,og5=og5,og6=og6,
                      da1=da1,da2=da2,da3=da3,da4=da4,da5=da5,da6=da6,
                      is1=is1,is2=is2,is3=is3,is4=is4,is5=is5,is6=is6,
                      im1=im1,im2=im2,im3=im3,im4=im4,im5=im5,im6=im6,
                      rm1=rm1,rm2=rm2,rm3=rm3,rm4=rm4,rm5=rm5,rm6=rm6,
                      empty1=empty1,empty2=empty2,empty3=empty3,empty4=empty4,empty5=empty5,empty6=empty6,
                      place1=place1, gate1=gate1, other1=other1)
    disp.save()
    return show_discipline(request)


def view_discipline(request):
    return render(request,'myapp/view_discipline.html')

def fetch_discipline(request):
    stu_id = request.POST.get('stu_id')
    my_res = Discipline.objects.filter(stu_id=stu_id)
    if len(my_res) == 0:
        return view_discipline(request)
    else:
        my_res = list(my_res)[0]
        return render(request,'myapp/view_discipline.html',{'my_res':my_res})

    return None