# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'School', fields ['name']
        db.delete_unique(u'schools_school', ['name'])

        # Adding field 'School.short_name'
        db.add_column(u'schools_school', 'short_name',
                      self.gf('django.db.models.fields.CharField')(default='Default', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'School.short_name'
        db.delete_column(u'schools_school', 'short_name')

        # Adding unique constraint on 'School', fields ['name']
        db.create_unique(u'schools_school', ['name'])


    models = {
        u'schools.school': {
            'Meta': {'object_name': 'School'},
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['schools']