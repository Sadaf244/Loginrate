from django.contrib import admin
from .models import Suser,loginhistory
from django.apps import apps

admin.site.register(Suser)
admin.site.register(loginhistory)
app=apps.get_app_config('graphql_auth')
for model_name,model in app.models.items():
    admin.site.register(model)