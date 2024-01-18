from django.contrib import admin
from users.models import (
    User,
    AdminData,
    AdminDomain,
    AreaOfInterest,
)

# Register your models here.
admin.site.register(User)
admin.site.register(AdminDomain)
admin.site.register(AdminData)
admin.site.register(AreaOfInterest)
