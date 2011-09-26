from django.conf.urls.defaults import *
from models import Weapon

from endless_pagination.views import AjaxListView
from views import GenericTableView, WeaponTable 

urlpatterns = patterns('',
            (r'^weapons/list/$', AjaxListView.as_view(model=Weapon,
                template_name='generic_list.html',
                page_template='generic_list_page.html')),
            (r'^weapons/table/$', GenericTableView.as_view(WeaponTable, model=Weapon)),
            )
