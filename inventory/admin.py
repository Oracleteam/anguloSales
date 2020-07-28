from django.contrib import admin
from inventory.models import *


# Register your models here.
@admin.register(product)
class productsAdmin(admin.ModelAdmin):
    """ admin model servers """
    list_display = ("shortName", "description", "pcost")

@admin.register(client)
class clientsAdmin(admin.ModelAdmin):
    """ admin model servers """
    list_display = ("name", "middleName", "lastName", "phone", "email")


class salesDetailInLine(admin.StackedInline):
    model = sale_detail
    can_delete = False
    verbose_name = 'Detalle de productos'


@admin.register(sale)
class salesAdmin(admin.ModelAdmin):
    """ admin model servers """
    #list_display = ("name", "middleName", "total", "createdOn", "createdOn")
    inlines = (salesDetailInLine,)


admin.site.index_title = "Welcome to Angulo Sales"
admin.site.site_header = "Angulo Sales Admin"
admin.site.site_title = "Angulo Sales Admin Portal"