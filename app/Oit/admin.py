from django.contrib import admin

from .models import Model_OIT, Model_MEDIO,Model_RED

# Register your models here.

admin.site.register(Model_OIT)

admin.site.register(Model_MEDIO)

admin.site.register(Model_RED)