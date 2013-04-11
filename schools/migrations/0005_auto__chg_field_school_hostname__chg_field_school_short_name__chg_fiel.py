# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'School.hostname'
        db.alter_column(u'schools_school', 'hostname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128))

        # Changing field 'School.short_name'
        db.alter_column(u'schools_school', 'short_name', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'School.name'
        db.alter_column(u'schools_school', 'name', self.gf('django.db.models.fields.CharField')(max_length=64))

    def backwards(self, orm):

        # Changing field 'School.hostname'
        db.alter_column(u'schools_school', 'hostname', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True))

        # Changing field 'School.short_name'
        db.alter_column(u'schools_school', 'short_name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'School.name'
        db.alter_column(u'schools_school', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'schools.school': {
            'Meta': {'object_name': 'School'},
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['schools']