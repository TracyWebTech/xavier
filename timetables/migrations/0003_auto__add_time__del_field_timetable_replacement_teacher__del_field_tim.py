# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Time'
        db.create_table(u'timetables_time', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timetable', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timetables.Timetable'])),
            ('start', self.gf('django.db.models.fields.TimeField')()),
            ('end', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'timetables', ['Time'])

        # Deleting field 'Timetable.replacement_teacher'
        db.delete_column(u'timetables_timetable', 'replacement_teacher_id')

        # Deleting field 'Timetable.start'
        db.delete_column(u'timetables_timetable', 'start')

        # Deleting field 'Timetable.end'
        db.delete_column(u'timetables_timetable', 'end')

        # Deleting field 'Timetable.weekday'
        db.delete_column(u'timetables_timetable', 'weekday')

        # Deleting field 'Timetable.day'
        db.delete_column(u'timetables_timetable', 'day')

        # Adding field 'Timetable.name'
        db.add_column(u'timetables_timetable', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Time'
        db.delete_table(u'timetables_time')

        # Adding field 'Timetable.replacement_teacher'
        db.add_column(u'timetables_timetable', 'replacement_teacher',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Teacher'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Timetable.start'
        db.add_column(u'timetables_timetable', 'start',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(7, 26, 10, 46256)),
                      keep_default=False)

        # Adding field 'Timetable.end'
        db.add_column(u'timetables_timetable', 'end',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(7, 26, 42, 65237)),
                      keep_default=False)

        # Adding field 'Timetable.weekday'
        db.add_column(u'timetables_timetable', 'weekday',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Timetable.day'
        db.add_column(u'timetables_timetable', 'day',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Timetable.name'
        db.delete_column(u'timetables_timetable', 'name')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.School']"})
        }
    }

    complete_apps = ['timetables']