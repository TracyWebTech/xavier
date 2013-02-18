# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("school", "0001_initial"),
    )

    def forwards(self, orm):
        # Adding model 'Period'
        db.create_table(u'period_period', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('year', self.gf('django.db.models.fields.DateTimeField')()),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.School'])),
        ))
        db.send_create_signal(u'period', ['Period'])

        # Adding model 'SubPeriod'
        db.create_table(u'period_subperiod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')()),
            ('period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['period.Period'])),
        ))
        db.send_create_signal(u'period', ['SubPeriod'])


    def backwards(self, orm):
        # Deleting model 'Period'
        db.delete_table(u'period_period')

        # Deleting model 'SubPeriod'
        db.delete_table(u'period_subperiod')


    models = {
        u'period.period': {
            'Meta': {'object_name': 'Period'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['school.School']"}),
            'year': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'period.subperiod': {
            'Meta': {'object_name': 'SubPeriod'},
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['period.Period']"}),
            'start': ('django.db.models.fields.DateField', [], {})
        },
        u'school.school': {
            'Meta': {'object_name': 'School'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['period']
