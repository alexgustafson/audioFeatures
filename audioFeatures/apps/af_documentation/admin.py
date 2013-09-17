from django.contrib import admin
from af_documentation.models import Section

class SectionAdmin(admin.ModelAdmin):

    list_display = ('title', )

admin.site.register(Section, SectionAdmin)