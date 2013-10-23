# -*- coding:utf-8 -*-
from django.db import models


class A(models.Model):
    field_a = models.CharField(verbose_name=u'Field A',
        max_length=255)
    field_b = models.PositiveSmallIntegerField(
        verbose_name=u'Field B', choices=[(0, u'Value 1',), (1, u'Value 2',)])

    def __unicode__(self):
        return u'%s - %s' % (self.field_a, self.get_field_b_display())

    @models.permalink
    def get_absolute_url(self):
        return ('edit_a', [unicode(self.pk)])


class B(models.Model):
    a = models.ForeignKey(A, verbose_name=u'Foreign key to A')
    field_a = models.URLField(verbose_name=u'Field A', blank=True)

    def __unicode__(self):
        return u'%s - %s' % (self.a, self.field_a)


class C(models.Model):
    b = models.ManyToManyField(B, related_name='c', blank=True, null=True)
    field_a = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return u'%s - %s' % (self.field_a, u' - '.join(
            [unicode(b) for b in self.b.all()]))
