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
            ('period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['periods.Period'], unique=True)),
        ))
        db.send_create_signal(u'calendars', ['Calendar'])

        # Adding model 'Break'
        db.create_table(u'calendars_break', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('calendar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calendars.Calendar'])),
            ('day', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'calendars', ['Break'])

        # Adding unique constraint on 'Break', fields ['calendar', 'day']
        db.create_unique(u'calendars_break', ['calendar_id', 'day'])


    def backwards(self, orm):
        # Removing unique constraint on 'Break', fields ['calendar', 'day']
        db.delete_unique(u'calendars_break', ['calendar_id', 'day'])

        # Deleting model 'Calendar'
        db.delete_table(u'calendars_calendar')

        # Deleting model 'Break'
        db.delete_table(u'calendars_break')


    models = {
        u'calendars.break': {
            'Meta': {'unique_together': "(('calendar', 'day'),)", 'object_name': 'Break'},
            'calendar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calendars.Calendar']"}),
            'day': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calendars.calendar': {
            'Meta': {'object_name': 'Calendar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['periods.Period']", 'unique': 'True'})
        },
        u'periods.period': {
            'Meta': {'unique_together': "(('name', 'year', 'school'),)", 'object_name': 'Period'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.School']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'schools.school': {
            'Meta': {'object_name': 'School'},
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['calendars']