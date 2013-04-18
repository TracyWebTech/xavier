# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SubPeriod.slug'
        db.add_column(u'periods_subperiod', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=30, unique=True, null=True),
                      keep_default=False)

        # Adding unique constraint on 'SubPeriod', fields ['name', 'period']
        db.create_unique(u'periods_subperiod', ['name', 'period_id'])

        # Adding unique constraint on 'Period', fields ['slug']
        db.create_unique(u'periods_period', ['slug'])

        # Adding unique constraint on 'Period', fields ['school', 'name', 'year']
        db.create_unique(u'periods_period', ['school_id', 'name', 'year'])


    def backwards(self, orm):
        # Removing unique constraint on 'Period', fields ['school', 'name', 'year']
        db.delete_unique(u'periods_period', ['school_id', 'name', 'year'])

        # Removing unique constraint on 'Period', fields ['slug']
        db.delete_unique(u'periods_period', ['slug'])

        # Removing unique constraint on 'SubPeriod', fields ['name', 'period']
        db.delete_unique(u'periods_subperiod', ['name', 'period_id'])

        # Deleting field 'SubPeriod.slug'
        db.delete_column(u'periods_subperiod', 'slug')


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