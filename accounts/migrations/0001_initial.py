# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("school", "0001_initial"),
        ("subject", "0001_initial"),
    )

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'accounts_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.School'])),
        ))
        db.send_create_signal(u'accounts', ['Student'])

        # Adding model 'Teacher'
        db.create_table(u'accounts_teacher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'accounts', ['Teacher'])

        # Adding M2M table for field subjects on 'Teacher'
        db.create_table(u'accounts_teacher_subjects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('teacher', models.ForeignKey(orm[u'accounts.teacher'], null=False)),
            ('subject', models.ForeignKey(orm[u'subject.subject'], null=False))
        ))
        db.create_unique(u'accounts_teacher_subjects', ['teacher_id', 'subject_id'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'accounts_student')

        # Deleting model 'Teacher'
        db.delete_table(u'accounts_teacher')

        # Removing M2M table for field subjects on 'Teacher'
        db.delete_table('accounts_teacher_subjects')


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

    complete_apps = ['accounts']
