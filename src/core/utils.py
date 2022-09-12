from django.contrib.contenttypes.models import ContentType

from .models import Transfer
from .settings import VERSION


def add_transfer(type, parameters, instance=None, user=None):
    transfer = Transfer(
        type=type,
        parameters=parameters,
        version=VERSION,
    )

    if instance:
        transfer.content_type = ContentType.objects.get_for_model(instance)
        transfer.object_id = instance.id

    if user:
        transfer.user = user

    transfer.save()
    return transfer
