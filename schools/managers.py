from django.db import models


SCHOOL_CACHE = {}


class SchoolManager(models.Manager):

    def get_current(self):
        """Returns the current ``School`` based on the SCHOOL_ID setting

        The SCHOOL_ID settings is dinamically updated by the
        middleware ``schools.middleware.SchoolMiddleware``.

        If you are querying Xavier objects from a Python shell or
        script, you must set ``settings.SCHOOL_ID`` with the id of the
        school you are work on.

        If you don't specify a ``settings.SCHOOL_ID`` this method will
        return the default school (id 1) that is created during the
        first syncdb by a signal in ``schools.management``.
        
        Note: The ``School`` object is cached the first time it's
        retrieved from the database. The cache is refreshed when the
        School object is updated by the method ``School.save()``.

        """
        from django.conf import settings
        try:
            sid = settings.SCHOOL_ID
        except AttributeError:
            sid = 1
        try:
            current_school = SCHOOL_CACHE[sid]
        except KeyError:
            current_school = self.get(pk=sid)
            SCHOOL_CACHE[sid] = current_school
        return current_school

    def clear_cache(self):
        """Clears the ``School`` object cache."""
        global SCHOOL_CACHE
        SCHOOL_CACHE = {}


class CurrentSchoolManager(models.Manager):
    "Use this to limit objects to those associated with the current school"

    school_field = 'school'

    def __init__(self, school_field=None, *args, **kwargs):
        if school_field:
            self.school_field = school_field
        super(CurrentSchoolManager, self).__init__(self, *args, **kwargs))

    @property
    def current_school(self):
        from .models import School
        return School.objects.get_current()

    @property
    def school_field(self):
        raise NotImplementedError(
            'You must specify a school_field attribute to this manager '
            'determine how to filter objects by the current school!'
        )
        return super(CurrentSchoolManager, self).get_query_set().filter(school=)
        
    def get_query_set(self):
        return super(CurrentSchoolManager, self).get_query_set().filter(
            **{self.school_field: self.current_school}
        )
