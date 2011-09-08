from django.contrib import admin

from models import Weapon, Armor, Commodity

class WeaponAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Generic', {
            'fields': (('_name', '_price', '_weight'),
                       ( '_image',),
                       ( '_description',),
                       ( 'tags',)
                       )
        }),
        ('Weaponstuff', {
            'fields': (('_damage', '_critical'),
                       ('_usefulness', '_type'),
                       ('_encumbrance', '_training'),
                       ('_range', '_ammunition')
                )
        }),
        ('Special', {
            #            'classes': ('collapse',),
            'classes': ('boolean_only',),
            'fields': (('_special_brace','_special_disarm','_special_monk', '_special_double',
                        '_special_reach','_special_trip','_special_nonlethal',), )
        }),
        )

    class Media:
       css = {
            "all": ("css/admin_custom.css",)
        }
    list_display = ('_name', '_price')

admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Armor)
admin.site.register(Commodity)
