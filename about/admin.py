from django.contrib import admin

# Register your models here.
from .models import About
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)