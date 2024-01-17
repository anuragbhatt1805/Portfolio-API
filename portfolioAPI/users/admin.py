from django.contrib import admin
from users.models import (
    User,
    AdminData,
    AdminDomain,
)

# Register your models here.
admin.site.register(User)
admin.site.register(AdminDomain)
admin.site.register(AdminData)
