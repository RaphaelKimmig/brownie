from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
# Create your models here.

class BaseItem(models.Model):
    _price = models.DecimalField(default=0, max_digits=32, decimal_places=2, verbose_name=_("Price in gold coins"))
    _weight = models.DecimalField(default=0, max_digits=32, decimal_places=1, verbose_name=_("Weight in pounds"))

    _name = models.CharField(max_length=255, default='')
    _description = models.TextField(blank=True, default='')

    _image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self._name




class Commodity(BaseItem):
    pass


WEAPON_TYPES = (
    ("bludgeoning", _("Bludgeoning")),
    ("piercing",_("Piercing")),
    ("slashing", _("Slashing")),
    ("piercing_slashing", _("Piercing and slashing"))
    )
    
WEAPON_CATEGORY = (
    ("meele", _("Meele")),
    ("projectile", _("Projectile")),
    ("thrown", _("Thrown")),
    ("thrown_only", _("Thrown only"))
    )

class Weapon(BaseItem):
    _damage = models.CharField(max_length=20)
    _critical = models.CharField(max_length=20)
    _type = models.CharField(max_length=20, choices=WEAPON_TYPES)
    
    
    # weapon specials
    _special_brace = models.BooleanField(default=False)
    _special_disarm = models.BooleanField(default=False)
    _special_monk = models.BooleanField(default=False)
    _special_double = models.BooleanField(default=False)
    _special_reach = models.BooleanField(default=False)
    _special_trip = models.BooleanField(default=False)
    _special_nonlethal = models.BooleanField(default=False)


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