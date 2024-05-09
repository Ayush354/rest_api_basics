from django.contrib import admin
import mainapp.models

admin.site.register(mainapp.models.Employee)
admin.site.register(mainapp.models.Student)
admin.site.register(mainapp.models.Passenger)