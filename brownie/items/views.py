# Create your views here.
from django_tables2.views import SingleTableMixin
from django.views.generic import ListView
import django_tables2 as tables

from models import Weapon

class WeaponTable(tables.Table):
    get_price = tables.Column()
    class Meta:
        model = Weapon
        exclude = ('id', '_image', '_description', '_special_disarm',
                '_special_brace',
                '_special_disarm','_special_monk','_special_double',
                '_special_reach','_special_trip','_special_nonlethal', )

class GenericTableView(SingleTableMixin, ListView):
    @classmethod
    def as_view(self, table_class, *args, **kwargs):
        self.table_class = table_class
        return super(GenericTableView, self).as_view(*args, **kwargs)
