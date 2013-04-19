# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.conf import settings

from schools import models


class CurrentSchoolMiddleware(object):

    def parse_host(self, host):
        """Returns ``(host, port)`` for a ``host`` in the form "host:port"

        If ``host`` does not have a port number, port will be
        ``None``.

        """
        if ':' in host:
            return host.rsplit(':', 1)
        return host, None

    def get_school(self, host):
        hostname, port = self.parse_host(host)
        try:
            return models.School.objects.get(hostname=hostname)
        except School.DoesNotExist:
            # The default school (id 1) is created during the
            # first syncdb by a signal in ``schools.management``.
            return get_object_or_404(School, pk=1)

    def process_request(self, request):
        host = request.get_host().lower()
        school = self.get_school(host)
        settings.SCHOOL_ID = school.pk
