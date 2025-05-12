from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

  date_hierarchy = 'created_at'
  list_filter = ('status', 'assigned')
  list_display = ('id', 'title', 'description', 'status', 'username_ticket', 'assigned', 'updated_at')
  search_fields = ['title','status']
  readonly_fields = ('image_preview',)

  def image_preview(self, obj):
    # ex. the name of column is "image"
    if obj.image:
        return mark_safe('<img src="{0}" width="90%" height="" style="object-fit:contain" />'.format(obj.image.url))
    else:
        return '(No image)'

  image_preview.short_description = 'Preview'
  

