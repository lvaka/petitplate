"""Admin module to register models."""
from django.contrib import admin
from menu import models

admin.site.register(models.Dish)
admin.site.register(models.Course)
admin.site.register(models.DishCourse)
admin.site.register(models.Menu)
admin.site.register(models.CourseMenu)
