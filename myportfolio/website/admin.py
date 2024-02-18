from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(About)
admin.site.register(Image)
admin.site.register(Skill)
admin.site.register(Certificate)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(ResumeList)