from django.contrib import admin
from .models import Users
from django.contrib.auth.admin import UserAdmin

admin.site.register(Users, UserAdmin)

UserAdmin.fieldsets[1][1]['fields'] = ("first_name", "last_name", "email", "address", 
                                        "phone", "receiver_name", "post_id", 'national_code', 
                                        'newsletter','card_number')
