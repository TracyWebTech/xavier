# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Period'
        db.create_table(u'periods_period', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('year', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.School'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True)),
        ))
        db.send_create_signal(u'periods', ['Period'])

        # Adding unique constraint on 'Period', fields ['name', 'year', 'school']
        db.create_unique(u'periods_period', ['name', 'year', 'school_id'])

        # Adding model 'SubPeriod'
        db.create_table(u'periods_subperiod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')()),
            ('period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['periods.Period'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=30, unique=True, null=True)),
        ))
        db.send_create_signal(u'periods', ['SubPeriod'])

        # Adding unique constraint on 'SubPeriod', fields ['name', 'period']
        db.create_unique(u'periods_subperiod', ['name', 'period_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'SubPeriod', fields ['name', 'period']
        db.delete_unique(u'periods_subperiod', ['name', 'period_id'])

        # Removing unique constraint on 'Period', fields ['name', 'year', 'school']
        db.delete_unique(u'periods_period', ['name', 'year', 'school_id'])

        # Deleting model 'Period'
        db.delete_table(u'periods_period')

        # Deleting model 'SubPeriod'
        db.delete_table(u'periods_subperiod')


    models = {
        u'periods.period': {
            'Meta': {'unique_together': "(('name', 'year', 'school'),)", 'object_name': 'Period'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.School']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'periods.subperiod': {
            'Meta': {'unique_together': "(('name', 'period'),)", 'object_name': 'SubPeriod'},
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['periods.Period']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'unique': 'True', 'null': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {})
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

    complete_apps = ['periods']