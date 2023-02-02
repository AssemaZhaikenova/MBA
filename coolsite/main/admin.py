from django.contrib import admin
from main.models import *
from django.contrib.auth.admin import UserAdmin

class StudentAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff', 'type'
        )
    pass

admin.site.register(Student, StudentAdmin)

class GroupInline(admin.StackedInline):
    model = GroupMember
    extra = 3

class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupInline]
    list_display = ["title"]


admin.site.register(Group, GroupAdmin)

admin.site.register(GroupMember)

admin.site.register(StudentType)

admin.site.register(Lesson)

admin.site.register(Request)

admin.site.register(LessonListeners)

admin.site.register(City)

admin.site.register(Teacher)

admin.site.register(RequestStatus)

admin.site.register(Discipline)

admin.site.register(Room)


