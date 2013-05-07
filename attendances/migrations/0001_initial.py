# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AttendanceBook'
        db.create_table(u'attendances_attendancebook', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classroom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Class'])),
            ('day', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'attendances', ['AttendanceBook'])

        # Adding unique constraint on 'AttendanceBook', fields ['classroom', 'day']
        db.create_unique(u'attendances_attendancebook', ['classroom_id', 'day'])

        # Adding model 'Attendance'
        db.create_table(u'attendances_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('attendance_book', self.gf('django.db.models.fields.related.ForeignKey')(related_name='attendances', to=orm['attendances.AttendanceBook'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(related_name='attendances', to=orm['accounts.Student'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='present', max_length=8)),
            ('explanation', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'attendances', ['Attendance'])

        # Adding unique constraint on 'Attendance', fields ['attendance_book', 'student']
        db.create_unique(u'attendances_attendance', ['attendance_book_id', 'student_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Attendance', fields ['attendance_book', 'student']
        db.delete_unique(u'attendances_attendance', ['attendance_book_id', 'student_id'])

        # Removing unique constraint on 'AttendanceBook', fields ['classroom', 'day']
        db.delete_unique(u'attendances_attendancebook', ['classroom_id', 'day'])

        # Deleting model 'AttendanceBook'
        db.delete_table(u'attendances_attendancebook')

        # Deleting model 'Attendance'
        db.delete_table(u'attendances_attendance')


    models = {
        u'accounts.student': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'object_name': 'Student', '_ormbases': [u'accounts.User']},
            'code': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'accounts.user': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'object_name': 'User'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.School']", 'null': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'attendances.attendance': {
            'Meta': {'unique_together': "(('attendance_book', 'student'),)", 'object_name': 'Attendance'},
            'attendance_book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attendances'", 'to': u"orm['attendances.AttendanceBook']"}),
            'explanation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'present'", 'max_length': '8'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attendances'", 'to': u"orm['accounts.Student']"})
        },
        u'attendances.attendancebook': {
            'Meta': {'unique_together': "(('classroom', 'day'),)", 'object_name': 'AttendanceBook'},
            'classroom': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Class']"}),
            'day': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounts.Student']", 'through': u"orm['attendances.Attendance']", 'symmetrical': 'False'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'classes.class': {
            'Meta': {'ordering': "['period', 'grade', 'identification']", 'unique_together': "(('identification', 'period', 'grade'),)", 'object_name': 'Class'},
            'grade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Grade']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['periods.Period']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '70', 'unique': 'True', 'null': 'True'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounts.Student']", 'symmetrical': 'False'})
        },
        u'classes.grade': {
            'Meta': {'ordering': "['grade_type', 'name']", 'unique_together': "(('name', 'grade_type'),)", 'object_name': 'Grade'},
            'grade_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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

    complete_apps = ['attendances']