# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Ammunition'
        db.create_table('items_ammunition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=2)),
            ('_weight', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=1)),
            ('_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('_description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('items', ['Ammunition'])

        # Adding field 'Weapon._usefulness'
        db.add_column('items_weapon', '_usefulness', self.gf('django.db.models.fields.CharField')(default='meele', max_length=255), keep_default=False)

        # Adding field 'Weapon._encumbrance'
        db.add_column('items_weapon', '_encumbrance', self.gf('django.db.models.fields.CharField')(default='one_handed', max_length=255), keep_default=False)

        # Adding field 'Weapon._training'
        db.add_column('items_weapon', '_training', self.gf('django.db.models.fields.CharField')(default='martial', max_length=255), keep_default=False)

        # Adding field 'Weapon._range'
        db.add_column('items_weapon', '_range', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding M2M table for field _ammunition on 'Weapon'
        db.create_table('items_weapon__ammunition', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('weapon', models.ForeignKey(orm['items.weapon'], null=False)),
            ('ammunition', models.ForeignKey(orm['items.ammunition'], null=False))
        ))
        db.create_unique('items_weapon__ammunition', ['weapon_id', 'ammunition_id'])

        # Changing field 'Weapon._type'
        db.alter_column('items_weapon', '_type', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Weapon._critical'
        db.alter_column('items_weapon', '_critical', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Weapon._damage'
        db.alter_column('items_weapon', '_damage', self.gf('django.db.models.fields.CharField')(max_length=255))


    def backwards(self, orm):
        
        # Deleting model 'Ammunition'
        db.delete_table('items_ammunition')

        # Deleting field 'Weapon._usefulness'
        db.delete_column('items_weapon', '_usefulness')

        # Deleting field 'Weapon._encumbrance'
        db.delete_column('items_weapon', '_encumbrance')

        # Deleting field 'Weapon._training'
        db.delete_column('items_weapon', '_training')

        # Deleting field 'Weapon._range'
        db.delete_column('items_weapon', '_range')

        # Removing M2M table for field _ammunition on 'Weapon'
        db.delete_table('items_weapon__ammunition')

        # Changing field 'Weapon._type'
        db.alter_column('items_weapon', '_type', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Weapon._critical'
        db.alter_column('items_weapon', '_critical', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Weapon._damage'
        db.alter_column('items_weapon', '_damage', self.gf('django.db.models.fields.CharField')(max_length=20))


    models = {
        'items.ammunition': {
            'Meta': {'object_name': 'Ammunition'},
            '_description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            '_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            '_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            '_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '2'}),
            '_weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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
            '_ammunition': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['items.Ammunition']", 'symmetrical': 'False'}),
            '_critical': ('django.db.models.fields.CharField', [], {'default': "'20/x2'", 'max_length': '255'}),
            '_damage': ('django.db.models.fields.CharField', [], {'default': "'1d8'", 'max_length': '255'}),
            '_description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            '_encumbrance': ('django.db.models.fields.CharField', [], {'default': "'one_handed'", 'max_length': '255'}),
            '_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            '_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            '_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '2'}),
            '_range': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            '_special_brace': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_disarm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_double': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_monk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_nonlethal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_reach': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_trip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_training': ('django.db.models.fields.CharField', [], {'default': "'martial'", 'max_length': '255'}),
            '_type': ('django.db.models.fields.CharField', [], {'default': "'slashing'", 'max_length': '255'}),
            '_usefulness': ('django.db.models.fields.CharField', [], {'default': "'meele'", 'max_length': '255'}),
            '_weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['items']
