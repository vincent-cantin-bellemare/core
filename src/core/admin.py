from django.contrib import admin

from . import models


class TransferAdmin(admin.ModelAdmin):
    fields = (
        'type',
        'parameters',
        'content_type',
        'object_id',
        'user',
        'mod_datetime',
        'add_datetime',
    )

    list_filter = (
        'type',
        'version',
        'user',
        'add_datetime',
    )

    search_fields = ('id',)

    list_display = (
        'id',
        'type',
        'version',
        'user',
        'add_datetime',
    )

    readonly_fields = (
        'add_datetime',
        'mod_datetime',
    )


admin.site.register(models.Transfer, TransferAdmin)
