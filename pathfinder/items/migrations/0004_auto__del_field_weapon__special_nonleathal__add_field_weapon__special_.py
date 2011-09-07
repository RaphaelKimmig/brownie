# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Weapon._special_nonleathal'
        db.delete_column('items_weapon', '_special_nonleathal')

        # Adding field 'Weapon._special_nonlethal'
        db.add_column('items_weapon', '_special_nonlethal', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Weapon._special_nonleathal'
        db.add_column('items_weapon', '_special_nonleathal', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Deleting field 'Weapon._special_nonlethal'
        db.delete_column('items_weapon', '_special_nonlethal')


    models = {
        'items.armor': {
            'Meta': {'object_name': 'Armor'},
            '_description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            '_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            '_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            '_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '2'}),
            '_weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'items.commodity': {
            'Meta': {'object_name': 'Commodity'},
            '_description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            '_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            '_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            '_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '2'}),
            '_weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'items.weapon': {
            'Meta': {'object_name': 'Weapon'},
            '_critical': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            '_damage': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            '_description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            '_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            '_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            '_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '2'}),
            '_special_brace': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_disarm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_double': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_monk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_nonlethal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_reach': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_trip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            '_weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['items']
