# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NonAttendance'
        db.create_table(u'attendances_nonattendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Student'])),
            ('class_subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.ClassSubject'])),
            ('day', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'attendances', ['NonAttendance'])


    def backwards(self, orm):
        # Deleting model 'NonAttendance'
        db.delete_table(u'attendances_nonattendance')


    models = {
        u'accounts.employee': {
            'Meta': {'object_name': 'Employee', '_ormbases': [u'accounts.User']},
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'accounts.student': {
            'Meta': {'object_name': 'Student', '_ormbases': [u'accounts.User']},
            'code': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'accounts.teacher': {
            'Meta': {'object_name': 'Teacher', '_ormbases': [u'accounts.Employee']},
            u'employee_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.Employee']", 'unique': 'True', 'primary_key': 'True'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['subjects.Subject']", 'symmetrical': 'False'})
        },
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
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
        u'attendances.nonattendance': {
            'Meta': {'object_name': 'NonAttendance'},
            'class_subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.ClassSubject']"}),
            'day': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Student']"})
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
            'Meta': {'object_name': 'Class'},
            'grade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Grade']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['periods.Period']"}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounts.Student']", 'symmetrical': 'False'})
        },
        u'classes.classsubject': {
            'Meta': {'object_name': 'ClassSubject'},
            'classroom': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Class']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['subjects.Subject']"}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Teacher']"})
        },
        u'classes.grade': {
            'Meta': {'object_name': 'Grade'},
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
        },
        u'subjects.subject': {
            'Meta': {'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['attendances']