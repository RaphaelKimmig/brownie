from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
# Create your models here.

class BaseItem(models.Model):
    price = models.DecimalField(default=0, max_digits=32, decimal_places=2, verbose_name=_("Price in gold coins"))
    weight = models.DecimalField(default=0, max_digits=32, decimal_places=1, verbose_name=_("Weight in pounds"))

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')

    image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name




class Commodity(BaseItem):
    pass


WEAPON_TYPES = (
    (0, _("Bludgeoning")),
    (1,_("Piercing")),
    (2, _("Slashing"))
    )
WEAPON_SPECIALS = (
    (0, _("Brace")),
    (1, _("Disarm")),
    (2, _("Double")),
    (3, _("Monk")),
    (4, _("Nonlethal")),
    (5, _("Reach")),
    (6, _("Trip")),
)

class Weapon(BaseItem):
    damage = models.CharField(max_length=20)
    critical = models.CharField(max_length=20)
    type = models.IntegerField(choices=WEAPON_TYPES)



class Armor(BaseItem):
    pass
