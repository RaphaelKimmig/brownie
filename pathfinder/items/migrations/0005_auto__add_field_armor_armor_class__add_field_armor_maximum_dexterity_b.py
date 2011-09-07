# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Armor.armor_class'
        db.add_column('items_armor', 'armor_class', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Armor.maximum_dexterity_bonus'
        db.add_column('items_armor', 'maximum_dexterity_bonus', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # Adding field 'Armor.armor_check_penalty'
        db.add_column('items_armor', 'armor_check_penalty', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Armor.arcane_spell_failure'
        db.add_column('items_armor', 'arcane_spell_failure', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # Adding field 'Armor.category'
        db.add_column('items_armor', 'category', self.gf('django.db.models.fields.CharField')(default=0, max_length=16), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Armor.armor_class'
        db.delete_column('items_armor', 'armor_class')

        # Deleting field 'Armor.maximum_dexterity_bonus'
        db.delete_column('items_armor', 'maximum_dexterity_bonus')

        # Deleting field 'Armor.armor_check_penalty'
        db.delete_column('items_armor', 'armor_check_penalty')

        # Deleting field 'Armor.arcane_spell_failure'
        db.delete_column('items_armor', 'arcane_spell_failure')

        # Deleting field 'Armor.category'
        db.delete_column('items_armor', 'category')


    models = {
        'items.armor': {
            'Meta': {'object_name': 'Armor'},
            '_description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            '_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            '_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            '_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '2'}),
            '_weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '1'}),
            'arcane_spell_failure': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'armor_check_penalty': ('django.db.models.fields.IntegerField', [], {}),
            'armor_class': ('django.db.models.fields.IntegerField', [], {}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maximum_dexterity_bonus': ('django.db.models.fields.PositiveIntegerField', [], {})
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
