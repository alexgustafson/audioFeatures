from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _

from af_documentation.models import Section

class AudioProcess(models.Model):
    name = models.CharField(_('Name'), max_length=120,)

    def __unicode__(self):
        return "%s" % self.name


class AudioProcessNode(MPTTModel):
    name = models.CharField(_('Name'), max_length=120,)
    audio_process = models.ForeignKey(AudioProcess)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertaion_by = ['name']

    def __unicode__(self):
        return "%s" % self.name


class AudioProcessChain(models.Model):
    name = models.CharField(_('Name'), max_length=120,)
    feature = models.ForeignKey(Section, related_name='process_chain')
    root_process = models.ForeignKey(AudioProcessNode)

    def __unicode__(self):
        return "%s" % self.name

