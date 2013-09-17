from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _
from django.contrib.comments import Comment

class Section(MPTTModel):
    title = models.CharField(_('Title'), max_length=120,)
    main_text = models.TextField(_('Main Text'), blank=True, null=True)
    order = models.IntegerField(_('Order'), blank=True, null=True)

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertaion_by = ['name']

    def __unicode__(self):
        return "%s" % self.title