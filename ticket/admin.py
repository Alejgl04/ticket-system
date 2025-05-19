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
  
  def get_queryset(self, request):
    qs = super().get_queryset(request)
    if request.user.is_superuser:
      return qs
    else:
      return qs.filter(assigned=request.user)
    
  def get_fields(self, request, obj=None):
    fields = super().get_fields(request, obj)
    if not request.user.is_superuser:  # Example: Hide fields from non-superusers
        fields_to_hide = ('assigned')
        fields = [f for f in fields if f not in fields_to_hide]
    return fields
  
  def get_form(self, request, obj=None, **kwargs):
    form = super().get_form(request, obj, **kwargs)
    if not request.user.is_superuser: # Replace 'specific_user'
      form.base_fields['username_ticket'].disabled = True  # Replace 'field1', etc
    return form

  def image_preview(self, obj):
    # ex. the name of column is "image"
    if obj.image:
        return mark_safe('<img src="{0}" width="90%" height="" style="object-fit:contain" />'.format(obj.image.url))
    else:
        return '(No image)'

  image_preview.short_description = 'Preview'
  

