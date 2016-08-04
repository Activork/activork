from django.contrib import admin
from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
    		# Override this to set the password to the value in the field if it's
    		# changed.
		print "save_model"
		print obj.has_usable_password()
		if obj.has_usable_password() == False:
			obj.set_password(obj.password)
		obj.first_name = obj.username
    		obj.save()

admin.site.register(MyUser,MyUserAdmin)


# Register your models here.
