from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
# Create your models here.
from taggit_autosuggest.managers import TaggableManager

class BaseItem(models.Model):
    _price = models.DecimalField(default=0, max_digits=32, decimal_places=2, verbose_name=_("Price in gold coins"))
    _weight = models.DecimalField(default=0, max_digits=32, decimal_places=1, verbose_name=_("Weight in pounds"))

    _name = models.CharField(max_length=255, default='', verbose_name=_("Name"))
    _description = models.TextField(blank=True, default='', verbose_name=_("Description"))

    _image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True, verbose_name=_("Image"))

    tags = TaggableManager()

    class Meta:
        abstract = True

    def __unicode__(self):
        return self._name
        
    def get_price(self):
        return _("%d gp") % int(self._price)
    get_price.short_description = _('Price')           
    get_price.admin_order_field = '_price'
    price = property(get_price)         

class Commodity(BaseItem):
    pass

WEAPON_TYPES = (
    ("bludgeoning", _("Bludgeoning")),
    ("piercing",_("Piercing")),
    ("slashing", _("Slashing")),
    ("piercing_or_slashing", _("Piercing or Slashing")),
    ("bludgeoning_or_piercing", _("Bludgeoning or Piercing")),
    ("bludgeoning_and_piercing", _("Bludgeoning and Piercing"))
    )
    
WEAPON_USEFULNESS = (
    ("meele", _("Meele")),
    ("projectile", _("Projectile")),
    ("thrown", _("Thrown")),
    ("thrown_only", _("Thrown only"))
    )
    
WEAPON_ENCUMBRANCE = (
    ("light", _("Light")),
    ("one_handed", _("One-Handed")),
    ("two_handed", _("Two-Handed"))
    )
    
WEAPON_TRAINING = (
    ("simple", _("Simple")),
    ("martial", _("Martial")),
    ("exotic", _("Exotic"))
    )
    
AMMUNITION_TYPES = (
    ("arrow", _("Arrow")),
    ("bolt", _("Bolt")),
    ("dart", _("Dart")),
    ("sling_bullet", _("Sling bullet"))
    )

class Weapon(BaseItem):
    _damage = models.CharField(max_length=255, default="1d8", verbose_name=_("Damage"))
    _critical = models.CharField(max_length=255, default="20/x2", verbose_name=_("Critical"))
    _type = models.CharField(max_length=255, choices=WEAPON_TYPES, default="slashing", verbose_name=_("Type"))
    _usefulness = models.CharField(max_length=255, choices=WEAPON_USEFULNESS, default="melee", verbose_name=_("Usefulness"))
    _encumbrance = models.CharField(max_length=255, choices=WEAPON_ENCUMBRANCE, default="one_handed", verbose_name=_("Encumbrance"))
    _training = models.CharField(max_length=255, choices=WEAPON_TRAINING, default="martial", verbose_name=_("Training"))
    _range = models.IntegerField(default=0, verbose_name=_("Range in feet"))
    _ammunition = models.CharField(max_length=255, choices=AMMUNITION_TYPES, blank=True, null=True, verbose_name=_("Ammunition"))
    
    # weapon specials
    _special_brace = models.BooleanField(default=False, verbose_name=_("Brace"))
    _special_disarm = models.BooleanField(default=False, verbose_name=_("Disarm"))
    _special_monk = models.BooleanField(default=False, verbose_name=_("Monk"))
    _special_double = models.BooleanField(default=False, verbose_name=_("Double"))
    _special_reach = models.BooleanField(default=False, verbose_name=_("Reach"))
    _special_trip = models.BooleanField(default=False, verbose_name=_("Trip"))
    _special_nonlethal = models.BooleanField(default=False, verbose_name=_("Nonlethal"))    
    
    def specials(self):
        special_list = ['brace', 'disarm', 'monk', 'double', 'reach', 'trip', 'nonlethal']
        output_list = []
        for special in special_list:
            field = '_special_%s' % special
            if getattr(self, field):
                verbose = self._meta.get_field_by_name(field)[0].verbose_name
                output_list.append(verbose)
        return ", ".join(output_list)
    specials.short_description = _("Specials")
    
class Ammunition(BaseItem):
    _type = models.CharField(max_length=255, default="arrow", verbose_name=_("Type"))

ARMOR_CATEGORIES = (
    ("light", _("Light")),
    ("medium", _("Medium")),
    ("heavy", _("Heavy")),
    ("shield", _("Shield")),
    ("extra", _("Extra")),
)

class Armor(BaseItem):
    armor_class = models.IntegerField(verbose_name=_("Armor class"))
    maximum_dexterity_bonus = models.PositiveIntegerField(verbose_name=_("Maximum dexterity bonus"))
    armor_check_penalty = models.IntegerField(verbose_name=_("Armor check penalty"))
    arcane_spell_failure = models.PositiveIntegerField(verbose_name=_("Arcane spell failure"))
    category = models.CharField(choices=ARMOR_CATEGORIES, verbose_name=("Category"), max_length=16)
