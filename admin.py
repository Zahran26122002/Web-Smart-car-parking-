from django.contrib import admin
from app1.models import Users,ParkingSlot,BookedSlot

# Register your models here.
admin.site.site_header = 'ParkAssist Administrator Homepage'
# class UsersAdmin(admin.ModelAdmin):
#     list_display = ('Name','Phone','Email','Vehiclenumber','Username','Password')

admin.site.register(Users)


admin.site.register(ParkingSlot)

admin.site.register(BookedSlot)



