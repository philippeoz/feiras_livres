import logging

from django.conf import settings


class LoggingMiddleware(object):
    """
    Middleware para gerar um log completo da api
    """
    _initial_http_body = None

    def __init__(self, get_response):
        self.get_response = get_response
        self.response = None
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        self.go_log(request, response)

        self.response = response

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_request(self, request):
        self._initial_http_body = request.body

    def go_log(self, request, response):
        """
        Adicionando log de request e response
        """
        if request.path.startswith('/feiras/') and \
            (request.method == "POST" and
                request.META.get('CONTENT_TYPE') == 'application/json' or
                request.method == "GET"):

            settings.REQUEST_LOGGER.log(
                logging.DEBUG,
                "GET: {}. body: {} response code: {}. "
                "response "
                "content: {}".format(
                    request.GET,
                    self._initial_http_body,
                    response.status_code,
                    response.content),
                extra={'tags': {'url': request.build_absolute_uri()}})
        return response
