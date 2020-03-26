from django.contrib import admin

from shop.models import Product, Producer, Comment

admin.site.register(Product)
admin.site.register(Producer)
admin.site.register(Comment)