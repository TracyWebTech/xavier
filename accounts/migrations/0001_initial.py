# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'accounts_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.School'], null=True)),
        ))
        db.send_create_signal(u'accounts', ['User'])

        # Adding M2M table for field groups on 'User'
        db.create_table(u'accounts_user_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'accounts.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(u'accounts_user_groups', ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        db.create_table(u'accounts_user_user_permissions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'accounts.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(u'accounts_user_user_permissions', ['user_id', 'permission_id'])

        # Adding model 'Student'
        db.create_table(u'accounts_student', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounts.User'], unique=True, primary_key=True)),
            ('code', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal(u'accounts', ['Student'])

        # Adding model 'Employee'
        db.create_table(u'accounts_employee', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounts.User'], unique=True, primary_key=True)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'accounts', ['Employee'])

        # Adding model 'Teacher'
        db.create_table(u'accounts_teacher', (
            (u'employee_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounts.Employee'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'accounts', ['Teacher'])

        # Adding M2M table for field subjects on 'Teacher'
        db.create_table(u'accounts_teacher_subjects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('teacher', models.ForeignKey(orm[u'accounts.teacher'], null=False)),
            ('subject', models.ForeignKey(orm[u'subjects.subject'], null=False))
        ))
        db.create_unique(u'accounts_teacher_subjects', ['teacher_id', 'subject_id'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'accounts_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table('accounts_user_groups')

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table('accounts_user_user_permissions')

        # Deleting model 'Student'
        db.delete_table(u'accounts_student')

        # Deleting model 'Employee'
        db.delete_table(u'accounts_employee')

        # Deleting model 'Teacher'
        db.delete_table(u'accounts_teacher')

        # Removing M2M table for field subjects on 'Teacher'
        db.delete_table('accounts_teacher_subjects')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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

    complete_apps = ['accounts']