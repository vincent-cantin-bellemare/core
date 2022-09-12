# -*- coding: utf-8 -*-

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('request', request)

        response = self.get_response(request)
        request.log.process_response(response)

        return response
