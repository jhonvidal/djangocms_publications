# coding : utf-8

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break
from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from cms.toolbar_base import CMSToolbar


@toolbar_pool.register
class BlogToolbar(CMSToolbar):
    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu('publications', _('Publications'))

        # Urls
        url_list_post = reverse('admin:publications_post_changelist')
        url_add_post = reverse('admin:publications_post_add')
        url_list_category = reverse('admin:publications_categorypost_changelist')
        url_add_category = reverse('admin:publications_categorypost_add')

        # Posts
        admin_menu.add_sideframe_item(_('Add post'), url=url_add_post)
        admin_menu.add_sideframe_item(_('Post list'), url=url_list_post)
        admin_menu.add_break()

        # Categories
        admin_menu.add_sideframe_item(_('Add category'), url=url_add_category)
        admin_menu.add_sideframe_item(_('Categories list'), url=url_list_category)
        admin_menu.add_break()
