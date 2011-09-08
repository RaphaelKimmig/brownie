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
            'fields': (('_special_brace','_special_disarm','_special_monk', '_special_double'),
                       ('_special_reach','_special_trip','_special_nonlethal',), )
        }),
        )

    list_display = ('_name', 'get_price', '_damage', '_critical', '_range', '_weight', '_type', 'specials')
    
    search_fields = ('_name', '_damage')
    list_filter = ('_type', '_usefulness', '_encumbrance', '_training', '_name')

admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Armor)
admin.site.register(Commodity)
