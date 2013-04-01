# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Calendar'
        db.create_table(u'calendars_calendar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['periods.Period'])),
        ))
        db.send_create_signal(u'calendars', ['Calendar'])

        # Adding model 'Break'
        db.create_table(u'calendars_break', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('calendar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calendars.Calendar'])),
            ('day', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'calendars', ['Break'])


    def backwards(self, orm):
        # Deleting model 'Calendar'
        db.delete_table(u'calendars_calendar')

        # Deleting model 'Break'
        db.delete_table(u'calendars_break')


    models = {
        u'calendars.break': {
            'Meta': {'object_name': 'Break'},
            'calendar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calendars.Calendar']"}),
            'day': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calendars.calendar': {
            'Meta': {'object_name': 'Calendar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['periods.Period']"})
        },
        u'periods.period': {
            'Meta': {'object_name': 'Period'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.School']"}),
            'year': ('django.db.models.fields.DateField', [], {})
        },
        u'schools.school': {
            'Meta': {'object_name': 'School'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['calendars']