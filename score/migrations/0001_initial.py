# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("classes", "0001_initial"),
    )

    def forwards(self, orm):
        # Adding model 'EvaluationCriteria'
        db.create_table(u'score_evaluationcriteria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('weight', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('class_subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.ClassSubject'])),
        ))
        db.send_create_signal(u'score', ['EvaluationCriteria'])

        # Adding model 'Score'
        db.create_table(u'score_score', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Student'])),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('criteria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['score.EvaluationCriteria'])),
            ('class_subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.ClassSubject'])),
            ('subperiod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['period.SubPeriod'])),
        ))
        db.send_create_signal(u'score', ['Score'])


    def backwards(self, orm):
        # Deleting model 'EvaluationCriteria'
        db.delete_table(u'score_evaluationcriteria')

        # Deleting model 'Score'
        db.delete_table(u'score_score')


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
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['subject.Subject']", 'symmetrical': 'False'})
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
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['school.School']", 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
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
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['period.Period']"}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounts.Student']", 'symmetrical': 'False'})
        },
        u'classes.classsubject': {
            'Meta': {'object_name': 'ClassSubject'},
            'classroom': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Class']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['subject.Subject']"}),
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
        u'period.period': {
            'Meta': {'object_name': 'Period'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['school.School']"}),
            'year': ('django.db.models.fields.DateField', [], {})
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
        },
        u'score.evaluationcriteria': {
            'Meta': {'object_name': 'EvaluationCriteria'},
            'class_subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.ClassSubject']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'weight': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'score.score': {
            'Meta': {'object_name': 'Score'},
            'class_subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.ClassSubject']"}),
            'criteria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['score.EvaluationCriteria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Student']"}),
            'subperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['period.SubPeriod']"})
        },
        u'subject.subject': {
            'Meta': {'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['score']
