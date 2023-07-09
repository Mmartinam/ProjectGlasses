from django.contrib import admin
from .models import Brand, Glasses, Client, Sales, Order

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    pass


admin.site.register(Brand, BrandAdmin)


class GlassesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Glasses, GlassesAdmin)


class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)


class SalesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sales, SalesAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)