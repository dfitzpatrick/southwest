# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Franchise'
        db.create_table(u'PJI_franchise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('dev_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('focus_group', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'PJI', ['Franchise'])

        # Adding model 'Store'
        db.create_table(u'PJI_store', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('franchise', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stores', to=orm['PJI.Franchise'])),
            ('store_id', self.gf('django.db.models.fields.IntegerField')(max_length=6)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('tgm_store', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
        ))
        db.send_create_signal(u'PJI', ['Store'])


    def backwards(self, orm):
        # Deleting model 'Franchise'
        db.delete_table(u'PJI_franchise')

        # Deleting model 'Store'
        db.delete_table(u'PJI_store')


    models = {
        u'PJI.franchise': {
            'Meta': {'object_name': 'Franchise'},
            'dev_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'focus_group': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'PJI.store': {
            'Meta': {'object_name': 'Store'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'franchise': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stores'", 'to': u"orm['PJI.Franchise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'store_id': ('django.db.models.fields.IntegerField', [], {'max_length': '6'}),
            'tgm_store': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['PJI']