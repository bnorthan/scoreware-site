from django.contrib import admin

# Register your models here.

from .models import Member
from .models import Race
from .models import Result

admin.site.register(Member)
admin.site.register(Race)
admin.site.register(Result)

class ResultAdminInline(admin.TabularInline):
    extra=0    
    search_fields=['last_name']
    model = Result

class RaceAdmin(admin.ModelAdmin):
    inlines = [ResultAdminInline]

admin.site.unregister(Race)
admin.site.register(Race, RaceAdmin)


