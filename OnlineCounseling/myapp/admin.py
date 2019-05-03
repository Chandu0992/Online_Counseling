from django.contrib import admin
from myapp.models import Student_Registration,Counselor,Add_Student,Feed_Back,pro_Question,Parent_View
from myapp.models import HOD
# Register your models here.

admin.site.register(Student_Registration)
admin.site.register(Counselor)
admin.site.register(Add_Student)
admin.site.register(Feed_Back)
admin.site.register(pro_Question)
admin.site.register(HOD)
admin.site.register(Parent_View)