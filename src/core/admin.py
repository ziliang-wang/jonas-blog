from django.contrib import admin
from django import forms
from .models import Profile, Category, Post, Comment, Slider
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
# Register your models here.

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'link', 'order')
    link_fields = ('title',)
    list_editable = ('order', )
    ordering = ('-order', 'id')


class ProfileAdmin(admin.ModelAdmin):
    """ 個人資料管理 """
    list_display = (
        'user',
        'fullname',
        'title',
        'email',
        'line',
        'weixin',
        'created'
    )
    ordering = ('-created',)


admin.site.register(Profile, ProfileAdmin)

class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'description': forms.Textarea
        }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ 分類管理 """
    form = CategoryAdminForm
    list_display = ('slug', 'name', 'order')
    list_editable = ('order',)


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'summary': forms.Textarea,
            'body': SummernoteWidget()
        }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ 博文管理 """
    form = PostAdminForm
    list_display = ('title', 'slug', 'category', 'views', 'flag', 'status', 'created')
    search_fields = ('title', 'body')
    list_filter = ('category', 'flag', 'status')
    date_hierarchy = 'created'
    ordering = ('-created', 'status')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ 評論管理 """
    list_display = ('post', 'name', 'ip', 'active', 'created')
    list_filter = ('active', 'created')
    ordering = ('-created',)