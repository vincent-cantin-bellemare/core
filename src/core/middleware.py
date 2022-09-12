# -*- coding: utf-8 -*-

import json

from django.utils import timezone

from .models import Transfer
from .utils import add_transfer


class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else None

        try:
            body = json.loads(request.body)
        except:
            body = None

        parameters = {
            'GET': request.GET,
            'POST': request.POST,
            'COOKIES': request.COOKIES,
            'META': {
                'HTTP_X_FORWARDED_FOR': request.META.get('HTTP_X_FORWARDED_FOR'),
                'REMOTE_ADDR': request.META.get('REMOTE_ADDR'),
                'HTTP_USER_AGENT': request.META.get('HTTP_USER_AGENT'),
                'HTTP_REFERER': request.META.get('HTTP_REFERER'),
            },
            'body': body,
            'absolute_url': request.build_absolute_uri(),
            'response': None,
        }

        transfer = add_transfer(Transfer.TYPE_REQUEST_LOG, parameters, None, user)
        from_datetime = timezone.now()
        response = self.get_response(request)
        to_datetime = timezone.now()
        duration = to_datetime - from_datetime
        total_seconds = round(duration.total_seconds(), 2)

        transfer.parameters['response'] = {
            'status_code': response.status_code,
            'total_seconds': total_seconds
        }
        transfer.save()

        return response
