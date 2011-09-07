# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Armor.description'
        db.delete_column('items_armor', 'description')

        # Deleting field 'Armor.weight'
        db.delete_column('items_armor', 'weight')

        # Deleting field 'Armor.price'
        db.delete_column('items_armor', 'price')

        # Deleting field 'Armor.image'
        db.delete_column('items_armor', 'image')

        # Deleting field 'Armor.name'
        db.delete_column('items_armor', 'name')

        # Adding field 'Armor._price'
        db.add_column('items_armor', '_price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=2), keep_default=False)

        # Adding field 'Armor._weight'
        db.add_column('items_armor', '_weight', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=1), keep_default=False)

        # Adding field 'Armor._name'
        db.add_column('items_armor', '_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Armor._description'
        db.add_column('items_armor', '_description', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Armor._image'
        db.add_column('items_armor', '_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'Commodity.description'
        db.delete_column('items_commodity', 'description')

        # Deleting field 'Commodity.weight'
        db.delete_column('items_commodity', 'weight')

        # Deleting field 'Commodity.price'
        db.delete_column('items_commodity', 'price')

        # Deleting field 'Commodity.image'
        db.delete_column('items_commodity', 'image')

        # Deleting field 'Commodity.name'
        db.delete_column('items_commodity', 'name')

        # Adding field 'Commodity._price'
        db.add_column('items_commodity', '_price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=2), keep_default=False)

        # Adding field 'Commodity._weight'
        db.add_column('items_commodity', '_weight', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=1), keep_default=False)

        # Adding field 'Commodity._name'
        db.add_column('items_commodity', '_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Commodity._description'
        db.add_column('items_commodity', '_description', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Commodity._image'
        db.add_column('items_commodity', '_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'Weapon.price'
        db.delete_column('items_weapon', 'price')

        # Deleting field 'Weapon.critical'
        db.delete_column('items_weapon', 'critical')

        # Deleting field 'Weapon.name'
        db.delete_column('items_weapon', 'name')

        # Deleting field 'Weapon.image'
        db.delete_column('items_weapon', 'image')

        # Deleting field 'Weapon.type'
        db.delete_column('items_weapon', 'type')

        # Deleting field 'Weapon.damage'
        db.delete_column('items_weapon', 'damage')

        # Deleting field 'Weapon.weight'
        db.delete_column('items_weapon', 'weight')

        # Deleting field 'Weapon.description'
        db.delete_column('items_weapon', 'description')

        # Adding field 'Weapon._price'
        db.add_column('items_weapon', '_price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=2), keep_default=False)

        # Adding field 'Weapon._weight'
        db.add_column('items_weapon', '_weight', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=1), keep_default=False)

        # Adding field 'Weapon._name'
        db.add_column('items_weapon', '_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Weapon._description'
        db.add_column('items_weapon', '_description', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Weapon._image'
        db.add_column('items_weapon', '_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Weapon._damage'
        db.add_column('items_weapon', '_damage', self.gf('django.db.models.fields.CharField')(default='', max_length=20), keep_default=False)

        # Adding field 'Weapon._critical'
        db.add_column('items_weapon', '_critical', self.gf('django.db.models.fields.CharField')(default='', max_length=20), keep_default=False)

        # Adding field 'Weapon._type'
        db.add_column('items_weapon', '_type', self.gf('django.db.models.fields.CharField')(default='slashing', max_length=20), keep_default=False)

        # Adding field 'Weapon._special_brace'
        db.add_column('items_weapon', '_special_brace', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Weapon._special_disarm'
        db.add_column('items_weapon', '_special_disarm', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Weapon._special_monk'
        db.add_column('items_weapon', '_special_monk', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Weapon._special_double'
        db.add_column('items_weapon', '_special_double', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Weapon._special_reach'
        db.add_column('items_weapon', '_special_reach', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Weapon._special_trip'
        db.add_column('items_weapon', '_special_trip', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Weapon._special_nonleathal'
        db.add_column('items_weapon', '_special_nonleathal', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Armor.description'
        db.add_column('items_armor', 'description', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Armor.weight'
        db.add_column('items_armor', 'weight', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=1), keep_default=False)

        # Adding field 'Armor.price'
        db.add_column('items_armor', 'price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=2), keep_default=False)

        # Adding field 'Armor.image'
        db.add_column('items_armor', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Armor.name'
        raise RuntimeError("Cannot reverse this migration. 'Armor.name' and its values cannot be restored.")

        # Deleting field 'Armor._price'
        db.delete_column('items_armor', '_price')

        # Deleting field 'Armor._weight'
        db.delete_column('items_armor', '_weight')

        # Deleting field 'Armor._name'
        db.delete_column('items_armor', '_name')

        # Deleting field 'Armor._description'
        db.delete_column('items_armor', '_description')

        # Deleting field 'Armor._image'
        db.delete_column('items_armor', '_image')

        # Adding field 'Commodity.description'
        db.add_column('items_commodity', 'description', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Commodity.weight'
        db.add_column('items_commodity', 'weight', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=1), keep_default=False)

        # Adding field 'Commodity.price'
        db.add_column('items_commodity', 'price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=2), keep_default=False)

        # Adding field 'Commodity.image'
        db.add_column('items_commodity', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Commodity.name'
        raise RuntimeError("Cannot reverse this migration. 'Commodity.name' and its values cannot be restored.")

        # Deleting field 'Commodity._price'
        db.delete_column('items_commodity', '_price')

        # Deleting field 'Commodity._weight'
        db.delete_column('items_commodity', '_weight')

        # Deleting field 'Commodity._name'
        db.delete_column('items_commodity', '_name')

        # Deleting field 'Commodity._description'
        db.delete_column('items_commodity', '_description')

        # Deleting field 'Commodity._image'
        db.delete_column('items_commodity', '_image')

        # Adding field 'Weapon.price'
        db.add_column('items_weapon', 'price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=2), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Weapon.critical'
        raise RuntimeError("Cannot reverse this migration. 'Weapon.critical' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Weapon.name'
        raise RuntimeError("Cannot reverse this migration. 'Weapon.name' and its values cannot be restored.")

        # Adding field 'Weapon.image'
        db.add_column('items_weapon', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Weapon.type'
        raise RuntimeError("Cannot reverse this migration. 'Weapon.type' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Weapon.damage'
        raise RuntimeError("Cannot reverse this migration. 'Weapon.damage' and its values cannot be restored.")

        # Adding field 'Weapon.weight'
        db.add_column('items_weapon', 'weight', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=32, decimal_places=1), keep_default=False)

        # Adding field 'Weapon.description'
        db.add_column('items_weapon', 'description', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Deleting field 'Weapon._price'
        db.delete_column('items_weapon', '_price')

        # Deleting field 'Weapon._weight'
        db.delete_column('items_weapon', '_weight')

        # Deleting field 'Weapon._name'
        db.delete_column('items_weapon', '_name')

        # Deleting field 'Weapon._description'
        db.delete_column('items_weapon', '_description')

        # Deleting field 'Weapon._image'
        db.delete_column('items_weapon', '_image')

        # Deleting field 'Weapon._damage'
        db.delete_column('items_weapon', '_damage')

        # Deleting field 'Weapon._critical'
        db.delete_column('items_weapon', '_critical')

        # Deleting field 'Weapon._type'
        db.delete_column('items_weapon', '_type')

        # Deleting field 'Weapon._special_brace'
        db.delete_column('items_weapon', '_special_brace')

        # Deleting field 'Weapon._special_disarm'
        db.delete_column('items_weapon', '_special_disarm')

        # Deleting field 'Weapon._special_monk'
        db.delete_column('items_weapon', '_special_monk')

        # Deleting field 'Weapon._special_double'
        db.delete_column('items_weapon', '_special_double')

        # Deleting field 'Weapon._special_reach'
        db.delete_column('items_weapon', '_special_reach')

        # Deleting field 'Weapon._special_trip'
        db.delete_column('items_weapon', '_special_trip')

        # Deleting field 'Weapon._special_nonleathal'
        db.delete_column('items_weapon', '_special_nonleathal')


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
            '_special_nonleathal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_reach': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_special_trip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            '_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            '_weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['items']
