from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Setting)
admin.site.register(Team)
admin.site.register(Services)
admin.site.register(Menu)


# customize reservation
# class ReservationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'date', 'time')



admin.site.register(Reservation)

admin.site.register(Client)



