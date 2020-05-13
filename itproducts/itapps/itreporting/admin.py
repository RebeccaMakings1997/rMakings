from django.contrib import admin
from .models import Review, Product, Upcoming_Products, Reviews_external

admin.site.register(Review)
admin.site.register(Product)
admin.site.register(Upcoming_Products)
admin.site.register(Reviews_external)

# Register your models here.

