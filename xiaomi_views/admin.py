from django.contrib import admin
from xiaomi_views.models import PhoneKind, PhoneDetail
# Register your models here.


class PhoneDetailAdmin(admin.ModelAdmin):
    pass


class PhoneKindlAdmin(admin.ModelAdmin):
    pass


admin.site.register(PhoneDetail, PhoneDetailAdmin)
admin.site.register(PhoneKind, PhoneKindlAdmin)