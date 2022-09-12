from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Transfer(models.Model):
    TYPE_AUTHENTICATION_LOG = 'authentication_log'
    TYPE_REQUEST_LOG = 'request_log'

    TYPES_CHOICES = (
        (TYPE_AUTHENTICATION_LOG, 'Authentication Log'),
        (TYPE_REQUEST_LOG, 'Request Log'),
    )

    version = models.CharField('version', null=False, blank=False, max_length=16)

    type = models.CharField('type', null=False, blank=False, max_length=255, choices=TYPES_CHOICES)
    parameters = models.JSONField('parameters', null=True, blank=True)

    content_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.SET_NULL)
    object_id = models.PositiveIntegerField('object id', null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    add_datetime = models.DateTimeField('add datetime', auto_now_add=True)
    mod_datetime = models.DateTimeField('mod datetime', auto_now=True)

    def __str__(self):
        return '#%5.5d (transfer)' % self.id if self.id else 'Transfer'
