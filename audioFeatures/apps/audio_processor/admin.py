from django.contrib import admin
from audio_processor.models import AudioProcess, AudioProcessChain, AudioProcessNode

class AudioProcessAdmin(admin.ModelAdmin):

    list_display = ('name', )

admin.site.register(AudioProcess, AudioProcessAdmin)

class AudioProcessChainAdmin(admin.ModelAdmin):

    list_display = ('name', )

admin.site.register(AudioProcessChain, AudioProcessChainAdmin)

class AudioProcessNodeAdmin(admin.ModelAdmin):

    list_display = ('name', )

admin.site.register(AudioProcessNode, AudioProcessNodeAdmin)