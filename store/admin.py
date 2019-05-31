from django.contrib import admin

# Register your models here.
from .models import MainCategory, Category, Product

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
class ProductInline(admin.StackedInline):
    model = Product
    extra = 3
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)