from django.contrib import admin

from app.dj_apps.users.models.users import VisuleoUser

admin.site.site_header = "Visuleo Admin"
admin.site.site_title = "Visuleo Admin Portal"
admin.site.index_title = "Welcome to Visuleo Portal"

admin.site.register(VisuleoUser)
