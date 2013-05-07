# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grade'
        db.create_table(u'classes_grade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('grade_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'classes', ['Grade'])

        # Adding unique constraint on 'Grade', fields ['name', 'grade_type']
        db.create_unique(u'classes_grade', ['name', 'grade_type'])

        # Adding model 'Class'
        db.create_table(u'classes_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identification', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['periods.Period'])),
            ('grade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Grade'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=70, unique=True, null=True)),
        ))
        db.send_create_signal(u'classes', ['Class'])

        # Adding unique constraint on 'Class', fields ['identification', 'period', 'grade']
        db.create_unique(u'classes_class', ['identification', 'period_id', 'grade_id'])

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
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['subjects.Subject'])),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Teacher'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=70, unique=True, null=True)),
        ))
        db.send_create_signal(u'classes', ['ClassSubject'])

        # Adding unique constraint on 'ClassSubject', fields ['classroom', 'subject']
        db.create_unique(u'classes_classsubject', ['classroom_id', 'subject_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ClassSubject', fields ['classroom', 'subject']
        db.delete_unique(u'classes_classsubject', ['classroom_id', 'subject_id'])

        # Removing unique constraint on 'Class', fields ['identification', 'period', 'grade']
        db.delete_unique(u'classes_class', ['identification', 'period_id', 'grade_id'])

        # Removing unique constraint on 'Grade', fields ['name', 'grade_type']
        db.delete_unique(u'classes_grade', ['name', 'grade_type'])

        # Deleting model 'Grade'
        db.delete_table(u'classes_grade')

        # Deleting model 'Class'
        db.delete_table(u'classes_class')

        # Removing M2M table for field students on 'Class'
        db.delete_table('classes_class_students')

        # Deleting model 'ClassSubject'
        db.delete_table(u'classes_classsubject')


    models = {
        u'accounts.employee': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'object_name': 'Employee', '_ormbases': [u'accounts.User']},
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'accounts.student': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'object_name': 'Student', '_ormbases': [u'accounts.User']},
            'code': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'accounts.teacher': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'object_name': 'Teacher', '_ormbases': [u'accounts.Employee']},
            u'employee_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.Employee']", 'unique': 'True', 'primary_key': 'True'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['subjects.Subject']", 'symmetrical': 'False'})
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
        u'classes.classsubject': {
            'Meta': {'unique_together': "(('classroom', 'subject'),)", 'object_name': 'ClassSubject'},
            'classroom': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Class']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '70', 'unique': 'True', 'null': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['subjects.Subject']"}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Teacher']"})
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
        },
        u'subjects.subject': {
            'Meta': {'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['classes']