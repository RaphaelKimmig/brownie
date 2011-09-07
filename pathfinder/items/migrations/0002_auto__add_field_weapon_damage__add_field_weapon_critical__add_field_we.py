# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Weapon.damage'
        db.add_column('items_weapon', 'damage', self.gf('django.db.models.fields.CharField')(default=0, max_length=20), keep_default=False)

        # Adding field 'Weapon.critical'
        db.add_column('items_weapon', 'critical', self.gf('django.db.models.fields.CharField')(default=0, max_length=20), keep_default=False)

        # Adding field 'Weapon.type'
        db.add_column('items_weapon', 'type', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Weapon.damage'
        db.delete_column('items_weapon', 'damage')

        # Deleting field 'Weapon.critical'
        db.delete_column('items_weapon', 'critical')

        # Deleting field 'Weapon.type'
        db.delete_column('items_weapon', 'type')


    models = {
        'items.armor': {
            'Meta': {'object_name': 'Armor'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '1'})
        },
        'items.commodity': {
            'Meta': {'object_name': 'Commodity'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '1'})
        },
        'items.weapon': {
            'Meta': {'object_name': 'Weapon'},
            'critical': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'damage': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '1'})
        }
    }

    complete_apps = ['items']
