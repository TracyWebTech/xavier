# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'School.hostname'
        db.add_column(u'schools_school', 'hostname',
                      self.gf('django.db.models.fields.CharField')(default='localhost', unique=True, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'School.hostname'
        db.delete_column(u'schools_school', 'hostname')


    models = {
        u'schools.school': {
            'Meta': {'object_name': 'School'},
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['schools']