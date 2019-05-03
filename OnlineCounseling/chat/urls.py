"""Chatting_App URL Configuration

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
from django.urls import path
from chat import views
urlpatterns = [

    path('show_std_index/',views.showIndex_Student,name='show_std_index'),
    path('show_cou_index/',views.showIndex_Counselor,name='show_cou_index'),
    path('show_hod_index/', views.showIndex_Hod, name='show_hod_index'),
    path('get_msg_student/',views.Get_Message_Student,name='get_msg_student'),
    path('get_msg_counselor/',views.Get_Message_Counselor,name='get_msg_counselor'),
    path('get_msg_hod/',views.Get_Message_HOD,name='get_msg_hod'),
    # path('upload/',views.upload,name='upload'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,documnet_root=settings.MEDIA_ROOT)
