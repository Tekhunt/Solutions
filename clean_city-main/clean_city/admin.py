from django.contrib import admin
from clean_city.models import User, Task, CheckList, CleaningArea


# Register your models here.
admin.site.register(CheckList)
admin.site.register(CleaningArea)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name',
                    'last_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    
    filter_vertical = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')

admin.site.register(Task, TaskAdmin)
