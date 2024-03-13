from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from .models import *
# Register your models here.


class WebsiteAdmin(admin.AdminSite):

    site_header = 'Shital Sapkota'
    site_title = 'Shital Sapkota'
    index_title = 'Admin Portfolio'


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


blog_site = WebsiteAdmin(name='BlogAdmin')

blog_site.register(NewUser, UserAdminConfig)
blog_site.register(About)
blog_site.register(Image)
blog_site.register(Skill)
blog_site.register(Certificate)
blog_site.register(Education)
blog_site.register(Experience)
blog_site.register(ResumeList)