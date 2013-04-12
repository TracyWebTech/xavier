# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Period.slug'
        db.add_column(u'periods_period', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=2013, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Period.slug'
        db.delete_column(u'periods_period', 'slug')


    models = {
        u'periods.period': {
            'Meta': {'object_name': 'Period'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.School']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'periods.subperiod': {
            'Meta': {'object_name': 'SubPeriod'},
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['periods.Period']"}),
            'start': ('django.db.models.fields.DateField', [], {})
        },
        u'schools.school': {
            'Meta': {'object_name': 'School'},
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['periods']