from django.db import models
from django.utils.translation import ugettext as _

class AudioFile(models.Model):
    title = models.CharField(_('Title'), max_length=256, )
    audiofile = models.FileField(_('Audio File'), upload_to='audiofiles', )

    def __unicode__(self):
        return "%s" % self.title

class ProcessFile(models.Model):
    title = models.CharField(_('Name'), max_length=256, )
    process_id = models.IntegerField(_('Process ID'), blank=True)
    process_file = models.FileField(_('file'), upload_to='audiofiles/processfiles', )

    parent = models.ForeignKey('AudioFile',)

    def __unicode__(self):
        return "%s" % self.title
