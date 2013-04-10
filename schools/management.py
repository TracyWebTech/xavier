"""Creates the default School object.

Based on ``django.contrib.sites.management``.

"""
from django.db.models import signals
from django.db import connections
from django.db import router
from django.core.management.color import no_style

from schools import models as school_app
from schools.models import School


def create_default_school(app, created_models, verbosity, db, **kwargs):
    # Only create the default schools in databases where Django created the table
    if School in created_models and router.allow_syncdb(db, School) :
        if verbosity >= 2:
            print("Creating the default School object")
        School(pk=1, name="Default School", hostname="localhost").save(using=db)

        # We set an explicit pk instead of relying on auto-incrementation,
        # so we need to reset the database sequence. See #17415.
        sequence_sql = connections[db].ops.sequence_reset_sql(no_style(), [School])
        if sequence_sql:
            if verbosity >= 2:
                print("Resetting sequence")
            cursor = connections[db].cursor()
            for command in sequence_sql:
                cursor.execute(command)

    School.objects.clear_cache()

signals.post_syncdb.connect(create_default_school, sender=school_app)
