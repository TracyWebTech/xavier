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
            'subperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['period.SubPeriod']"})
        },
        u'subject.subject': {
            'Meta': {'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['score']
