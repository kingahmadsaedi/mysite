from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post,Category

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','auther','counted_view','status','publish_date','created_date')
    list_filter=('status',)
    #ordering=['-created_date']
    search_fields=['title','content']
    summernote_fields = ('content',)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)