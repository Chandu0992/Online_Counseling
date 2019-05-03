from django.shortcuts import render
from chat.models import Text_Message
from myapp.models import Add_Student
import datetime
#from django.core.files.storage import FileSystemStorage
# Create your views here.

def showIndex_Student(request):
    stu_id = request.session.get('stu_id')
    cou_id = Add_Student.objects.filter(student_id=stu_id)
    cou_id = list(cou_id)[0]
    cou_id = cou_id.counselor_id

    #Concat Ids
    stu_msg_id = stu_id + '_' + cou_id
    cou_msg_id = cou_id + '_' + stu_id

    #Session Creation
    request.session['stu_msg_id'] = stu_msg_id
    request.session['cou_msg_id'] = cou_msg_id

    #Fetch Messages
    sms_group = Text_Message.objects.filter(user_id__in=[request.session.get('stu_msg_id'), request.session.get('cou_msg_id')]).order_by('dt_time')


    if len(sms_group) == 0:
        return render(request, 'chat/index_student.html')
    else:
        sms_group = list(sms_group)
        my_id = request.session.get('stu_msg_id')
        print("my id : ",my_id)
        return render(request, 'chat/index_student.html', {'sms': sms_group,'my_id':my_id})

def showIndex_Hod(request):
    if request.method == 'POST':
        stu_id = request.POST.get('student_id')
        hod_id = request.session.get('hod_id')
        stu_msg_id = stu_id +'_'+hod_id
        hod_msg_id = hod_id +'_'+ stu_id
        # Session Creation
        request.session['stu_msg_id'] = stu_msg_id
        request.session['hod_msg_id'] = hod_msg_id

        #Fetching Data
        sms_group = Text_Message.objects.filter(user_id__in=[request.session.get('hod_msg_id'), request.session.get('stu_msg_id')]).order_by('dt_time')

        if len(sms_group) == 0:
            return render(request, 'chat/index_hod.html')
        else:
            sms_group = list(sms_group)
            my_id = request.session.get('hod_msg_id')
            print("my id : ", my_id)
            return render(request, 'chat/index_hod.html', {'sms': sms_group, 'my_id': my_id})
    else:
        sms_group = Text_Message.objects.filter(user_id__in=[request.session.get('hod_msg_id'), request.session.get('stu_msg_id')]).order_by('dt_time')

        if len(sms_group) == 0:
            return render(request, 'chat/index_hod.html')
        else:
            sms_group = list(sms_group)
            my_id = request.session.get('hod_msg_id')
            return render(request, 'chat/index_hod.html', {'sms': sms_group, 'my_id': my_id})


def showIndex_Counselor(request):
    if request.method == 'POST':
        stu_id = request.POST.get('student_id')
        cou_id = request.session.get('cou_id')
        stu_msg_id = stu_id + '_' + cou_id
        cou_msg_id = cou_id + '_' + stu_id
        # Session Creation
        request.session['stu_msg_id'] = stu_msg_id
        request.session['cou_msg_id'] = cou_msg_id

        # Fetching Data
        sms_group = Text_Message.objects.filter(
            user_id__in=[request.session.get('cou_msg_id'), request.session.get('stu_msg_id')]).order_by('dt_time')

        if len(sms_group) == 0:
            return render(request, 'chat/index_counselor.html')
        else:
            sms_group = list(sms_group)
            my_id = request.session.get('cou_msg_id')
            print("my id : ", my_id)
            return render(request, 'chat/index_counselor.html', {'sms': sms_group, 'my_id': my_id})
    else:
        sms_group = Text_Message.objects.filter(user_id__in=[request.session.get('cou_msg_id'), request.session.get('stu_msg_id')]).order_by('dt_time')

        if len(sms_group) == 0:
            return render(request, 'chat/index_counselor.html')
        else:
            sms_group = list(sms_group)
            my_id = request.session.get('cou_msg_id')
            return render(request, 'chat/index_counselor.html', {'sms': sms_group, 'my_id': my_id})

def Get_Message_Student(request):
    id = request.session.get('stu_msg_id')
    print("Sms Save Method Student id : ",id)
    msg = request.POST.get('my_sms')
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    res = Text_Message(user_id=id, message=msg, dt_time=now)
    res.save()
    return thankYou_Student(request)

def Get_Message_Counselor(request):
    id = request.session.get('cou_msg_id')
    msg = request.POST.get('my_sms')
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    res = Text_Message(user_id=id, message=msg, dt_time=now)
    res.save()
    return thankYou_Counselor(request)

def Get_Message_HOD(request):
    id = request.session.get('hod_msg_id')
    msg = request.POST.get('my_sms')
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    res = Text_Message(user_id=id, message=msg, dt_time=now)
    res.save()
    return thankYou(request)

def thankYou(request):
    return render(request, 'chat/success.html')

def thankYou_Counselor(request):
    return render(request, 'chat/success_counselor.html')

def thankYou_Student(request):
    return render(request, 'chat/success_student.html')