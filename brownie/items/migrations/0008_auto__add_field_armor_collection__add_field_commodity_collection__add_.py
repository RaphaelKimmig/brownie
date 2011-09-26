# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    # we can't have a dry run because we need to create/get the campaign
    no_dry_run = True
    # we need this to create the related campaign
    depends_on = (
                    ("campaign", "0001_initial"),
                    )

    def forwards(self, orm):
        collection, created = orm['campaign.Collection'].objects.get_or_create(name="default collection")

        # Adding field 'Armor.collection'
        db.add_column('items_armor', 'collection', self.gf('django.db.models.fields.related.ForeignKey')(default=collection.pk, to=orm['campaign.Collection']), keep_default=False)

        # Adding field 'Commodity.collection'
        db.add_column('items_commodity', 'collection', self.gf('django.db.models.fields.related.ForeignKey')(default=collection.pk, to=orm['campaign.Collection']), keep_default=False)

        # Adding field 'Weapon.collection'
        db.add_column('items_weapon', 'collection', self.gf('django.db.models.fields.related.ForeignKey')(default=collection.pk, to=orm['campaign.Collection']), keep_default=False)

        # Changing field 'Weapon._critical'
        db.alter_column('items_weapon', '_critical', self.gf('django.db.models.fields.CharField')(max_length=16))

        # Changing field 'Weapon._damage'
        db.alter_column('items_weapon', '_damage', self.gf('django.db.models.fields.CharField')(max_length=16))

        # Adding field 'Ammunition.collection'
        db.add_column('items_ammunition', 'collection', self.gf('django.db.models.fields.related.ForeignKey')(default=collection.pk, to=orm['campaign.Collection']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Armor.collection'
        db.delete_column('items_armor', 'collection_id')

        # Deleting field 'Commodity.collection'
        db.delete_column('items_commodity', 'collection_id')

        # Deleting field 'Weapon.collection'
        db.delete_column('items_weapon', 'collection_id')

        # Changing field 'Weapon._critical'
        db.alter_column('items_weapon', '_critical', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Weapon._damage'
        db.alter_column('items_weapon', '_damage', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Deleting field 'Ammunition.collection'
        db.delete_column('items_ammunition', 'collection_id')


    models = {
        'campaign.collection': {
            'Meta': {'object_name': 'Collection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'items.ammunition': {
            'Meta': {'object_name': 'Ammunition'},
            '_description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            '_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            '_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            '_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '2'}),
            '_type': ('django.db.models.fields.CharField', [], {'default': "'arrow'", 'max_length': '255'}),
            '_weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '1'}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['campaign.Collection']"}),
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
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['campaign.Collection']"}),
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
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['campaign.Collection']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'items.weapon': {
            'Meta': {'object_name': 'Weapon'},
            '_ammunition': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            '_critical': ('django.db.models.fields.CharField', [], {'default': "'20/x2'", 'max_length': '16'}),
            '_damage': ('django.db.models.fields.CharField', [], {'default': "'1d8'", 'max_length': '16'}),
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
            '_usefulness': ('django.db.models.fields.CharField', [], {'default': "'melee'", 'max_length': '255'}),
            '_weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '1'}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['campaign.Collection']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_items'", 'to': "orm['taggit.Tag']"})
        }
    }

    complete_apps = ['items']
