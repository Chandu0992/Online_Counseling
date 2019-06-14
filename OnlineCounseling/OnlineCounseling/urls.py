"""OnlineCounseling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from myapp import views
urlpatterns = [
    #Admin Views
    path('admin/', admin.site.urls),
    #Student and Counselor Views
    path('',views.showIndex,name='index'),
    path('show_reg_student/',views.Show_Register_Student,name='show_reg_student'),
    path('reg_student/',views.Register_Student,name='reg_student'),
    path('show_counselor/',views.show_counselor,name='show_counselor'),
    path('fetch_counselor/',views.fetch_counselor,name='fetch_counselor'),
    path('reg_counselor/',views.reg_counselor,name='reg_counselor'),
    path('login_counselor/',views.login_counselor,name='login_counselor'),
    path('add_student/',views.addStudent,name='add_student'),
    path('addStudent_hod/',views.addStudent_hod,name='addStudent_hod'),
    path('show_feed_back/',views.show_feed_back,name='show_feed_back'),
    path('get_feed_back/',views.get_feed_back,name='get_feed_back'),
    path('view_feed_back/',views.view_feed_back,name='view_feed_back'),
    path('view_feed_back_hod/',views.view_feed_back_hod,name='view_feed_back_hod'),
    path('view_student/',views.view_student,name='view_student'),
    path('view_student_hod/',views.view_student_hod,name='view_student_hod'),
    path('show_ask_question/',views.show_ask_question,name='show_ask_question'),
    path('show_ask_question_hod/',views.show_ask_question_hod,name='show_ask_question_hod'),
    path('get_question/',views.get_Question,name='get_question'),
    path('get_question_hod/',views.get_Question_hod,name='get_question_hod'),
    path('student_login/',views.student_Login,name='student_login'),
    path('otp_verification/',views.student_login_verification,name='otp_verification'),
    path('otp_confirmation/',views.student_login_confirmation,name='otp_confirmation'),
    path('upload/',views.upload,name='upload'),
    path('student_home/',views.student_home,name='student_home'),
    path('student_Questions/',views.student_Questions,name='student_Questions'),
    path('show_student_Questions/',views.show_student_Questions,name='show_student_Questions'),
    path('student_logout/',views.Student_Logout,name='student_logout'),
    path('show_pro_que/',views.show_pro_que,name='show_pro_que'),
    path('ans_to_counselor/',views.ans_to_counselor,name='ans_to_counselor'),
    path('show_stu_que/',views.show_stu_que,name='show_stu_que'),
    path('show_stu_que_hod/',views.show_stu_que_hod,name='show_stu_que_hod'),
    path('ans_to_student/',views.ans_to_student,name='ans_to_student'),
    path('counselor_logout/',views.Counselor_Logout,name='counselor_logout'),
    path('show_performance/',views.show_student_performance,name='show_performance'),
    path('add_performance/',views.add_performance,name='add_performance'),
    #Hod Views
    path('hod_logout/',views.Hod_Logout,name='hod_logout'),
    path('show_hod',views.show_hod,name='show_hod'),
    path('reg_hod/',views.reg_hod,name='reg_hod'),
    path('login_hod/',views.login_hod,name='login_hod'),
    path('hod_home/',views.fetch_hod,name='hod_home'),
    path('show_feedback_all/',views.show_feedback_all_students,name='show_feedback_all'),
    #Chat Views
    path('my_chat/',include('chat.urls')),
    #parent Views
    path('show_parent/',views.show_parent,name='show_parent'),
    path('show_student_list/',views.show_student_list,name='show_student_list'),
    path('show_my_graph/',views.show_my_graph,name='show_my_graph'),
    #Student Marks Views
    path('show_academic/', views.show_academic_year, name='show_academic'),
    path('add_academic_year/',views.add_academic_year,name='add_academic_year'),
    path('Show_academic_year/',views.Show_academic_year,name='Show_academic_year'),
    path('fetch_Student_academic_detail',views.fetch_Student_academic_detail,name='fetch_Student_academic_detail'),
    path('show_counseling_record/',views.show_counseling_record,name='show_counseling_record'),
    path('counseling_record/',views.counseling_record,name='counseling_record'),
    path('fetch_counselor_record/',views.fetch_counselor_record,name='fetch_counselor_record'),
    path('show_fetch_counselor_record/',views.show_fetch_counselor_record,name='show_fetch_counselor_record'),
    path('show_discipline/',views.show_discipline,name='show_discipline'),
    path('get_discipline/',views.get_discipline,name='get_discipline'),
    path('viw_discipline/',views.view_discipline,name='view_discipline'),
    path('fetch_discipline/',views.fetch_discipline,name='fetch_discipline'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,documnet_root=settings.MEDIA_ROOT)
