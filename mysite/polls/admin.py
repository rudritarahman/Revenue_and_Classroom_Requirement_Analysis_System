from django.contrib import admin

# Register your models here.
from .models import School_T
from .models import Department_T
from .models import Faculty_T
from .models import Course_T
from .models import CoOfferedCourse_T
from .models import Room_T
from .models import Section_T

admin.site.register(School_T)
admin.site.register(Department_T)
admin.site.register(Faculty_T)
admin.site.register(Course_T)
admin.site.register(CoOfferedCourse_T)
admin.site.register(Room_T)
admin.site.register(Section_T)