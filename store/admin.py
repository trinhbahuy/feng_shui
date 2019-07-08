from django.contrib import admin

# Register your models here.
from .models import MainCategory, Category, Product

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
class ProductInline(admin.StackedInline):
    model = Product
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

class CategoryInline(admin.StackedInline):
    model = Category
    extra = 1

class MainCategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]

admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)