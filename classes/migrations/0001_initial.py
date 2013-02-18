# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("accounts", "0001_initial"),
    )

    def forwards(self, orm):
        # Adding model 'Grade'
        db.create_table(u'classes_grade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('grade_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'classes', ['Grade'])

        # Adding model 'Class'
        db.create_table(u'classes_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identification', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['period.Period'])),
            ('grade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Grade'])),
        ))
        db.send_create_signal(u'classes', ['Class'])

        # Adding M2M table for field students on 'Class'
        db.create_table(u'classes_class_students', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('class', models.ForeignKey(orm[u'classes.class'], null=False)),
            ('student', models.ForeignKey(orm[u'accounts.student'], null=False))
        ))
        db.create_unique(u'classes_class_students', ['class_id', 'student_id'])

        # Adding model 'ClassSubject'
        db.create_table(u'classes_classsubject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classroom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Class'])),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['subject.Subject'])),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Teacher'])),
        ))
        db.send_create_signal(u'classes', ['ClassSubject'])


    def backwards(self, orm):
        # Deleting model 'Grade'
        db.delete_table(u'classes_grade')

        # Deleting model 'Class'
        db.delete_table(u'classes_class')

        # Removing M2M table for field students on 'Class'
        db.delete_table('classes_class_students')

        # Deleting model 'ClassSubject'
        db.delete_table(u'classes_classsubject')


    models = {
        u'accounts.student': {
            'Meta': {'object_name': 'Student'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['school.School']"})
        },
        u'accounts.teacher': {
            'Meta': {'object_name': 'Teacher'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['subject.Subject']", 'symmetrical': 'False'})
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
        u'period.period': {
            'Meta': {'object_name': 'Period'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['school.School']"}),
            'year': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'school.school': {
            'Meta': {'object_name': 'School'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'subject.subject': {
            'Meta': {'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['classes']
