from django.contrib import admin
from audio.models import AudioFile

class AudioFileAdmin(admin.ModelAdmin):

    list_display = ('title', )

admin.site.register(AudioFile, AudioFileAdmin)