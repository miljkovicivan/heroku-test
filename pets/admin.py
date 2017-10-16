from django.contrib import admin
from django.contrib.auth.models import User

from .models import Cat, Dog

admin.site.register(Cat)
admin.site.register(Dog)
admin.site.unregister(User)

class CatInline(admin.TabularInline):
    model = Cat

class DogInline(admin.TabularInline):
    model = Dog

class Owner(admin.ModelAdmin):
    inlines = [
        CatInline,
        DogInline,
    ]

admin.site.register(User, Owner)
