# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Timetable.slug'
        db.add_column(u'timetables_timetable', 'slug',
                      self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=100),
                      keep_default=False)

        # Adding unique constraint on 'Timetable', fields ['name']
        db.create_unique(u'timetables_timetable', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Timetable', fields ['name']
        db.delete_unique(u'timetables_timetable', ['name'])

        # Deleting field 'Timetable.slug'
        db.delete_column(u'timetables_timetable', 'slug')


    models = {
        u'schools.school': {
            'Meta': {'object_name': 'School'},
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'})
        },
        u'timetables.time': {
            'Meta': {'object_name': 'Time'},
            'end': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'timetable': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timetables.Timetable']"})
        },
        u'timetables.timetable': {
            'Meta': {'object_name': 'Timetable'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.School']"}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['timetables']